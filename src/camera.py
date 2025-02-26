import cv2
import numpy as np
import pyautogui
from typing import Tuple, List
from time import sleep, time as now
import easyocr

from utils import logger
from config import config
from enums import Button, Text
from enums import WaitForResults

if config.isWindows():
  import dxcam

class Camera:
  WIDTH = 1280
  HEIGHT = 720
  REGION = (0, 0, WIDTH, HEIGHT)
  THRESHOLD = 0.7

  camera = None
  ocr = None

  def __init__(self) -> None:
    if config.isWindows():
      self.camera = dxcam.create(output_color='RGB', output_idx=0)
      self.ocr = easyocr.Reader(['en'], gpu=True)

  def grab(self, region = REGION):
    if config.isWindows():
      return self.camera.grab(region)

    if config.isMac():
      return np.array(pyautogui.screenshot(region=self.REGION))

  def _matchTemplate(self, frame, template):
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= self.THRESHOLD)
    return [[int(positions[0]), int(positions[1])] for positions in zip(*loc[::-1])]

  def _prepareForGroup(self, positions, templateW, templateH):
    return [[position[0], position[1], templateW, templateH] for position in positions]

  def _group(self, positions):
    return cv2.groupRectangles(positions, 1, 0.2)

  def find(self, frame, template) -> Tuple[int, int, int, int]:
    positions = self._matchTemplate(frame, template)
    positions = self._prepareForGroup(positions, template.shape[1], template.shape[0])
    positions, _ = self._group(positions)

    if len(positions):
      (x, y, w, h) = positions[0]
      return (int(x), int(y), int(x + w), int(y + h))

    return None

  def showImage(self, frame):
    WINDOW_NAME = 'GAME'
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    # cv2.resizeWindow(WINDOW_NAME, self.WIDTH // 2, self.HEIGHT // 2)
    cv2.moveWindow(WINDOW_NAME, self.WIDTH, 0)

    while True:

      cv2.imshow(WINDOW_NAME, frame)
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    cv2.destroyAllWindows()

  def waitFor(self, type: Button | Text, timeout: int = 240) -> Tuple[WaitForResults, Tuple[int, int, int, int]]:
    logger.info(f"Waiting for {type}")
    template = cv2.imread(type.value, cv2.IMREAD_GRAYSCALE)

    # Crash detection
    relaunchButton = cv2.imread(Button.RELAUNCH.value, cv2.IMREAD_GRAYSCALE)

    # Idle detection
    keepPlayingButton = cv2.imread(Button.KEEP_PLAYING.value, cv2.IMREAD_GRAYSCALE)

    # Claim stars
    claimStars = cv2.imread(Button.CLAIM.value, cv2.IMREAD_GRAYSCALE)

    startTime = now()

    while True and now() - startTime < timeout:
        frame = self.grab()

        if frame is None:
          continue

        position = self.find(frame, template)

        relaunchButtonPos = self.find(frame, relaunchButton)
        if relaunchButtonPos:
          logger.info('Crash detected')
          return WaitForResults.CRASH, relaunchButtonPos

        keepPlayingButtonPos = self.find(frame, keepPlayingButton)
        if keepPlayingButtonPos:
          logger.info('KeepPlaying detected')
          return WaitForResults.SLEEP, keepPlayingButtonPos

        claimStarsPos = self.find(frame, claimStars)
        if claimStarsPos:
          logger.info('Claim Stars detected')
          return WaitForResults.CLAIM, claimStarsPos

        if position:
          logger.info(f'Step {type} found')
          return WaitForResults.POSITION, position

        sleep(2)

    logger.info(f"waitFor() - {timeout}s timeout")
    return None, None

  def readText(self, frame) -> List[str]:
    return self.ocr.readtext(frame, detail=0)
    pass

camera = Camera()
