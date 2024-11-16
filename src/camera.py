import dxcam
import cv2
import numpy as np
from typing import Tuple
from time import sleep, time as now
from enums import Button, Text
from utils import logger

class Camera:
  WIDTH = 1280
  HEIGHT = 720
  REGION = (0, 0, WIDTH, HEIGHT)
  THRESHOLD = 0.7

  camera = None

  def __init__(self) -> None:
    self.camera = dxcam.create(output_color='RGB', output_idx=0)

  def grab(self, region = REGION):
    return self.camera.grab(region)

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

  def waitFor(self, type: Button | Text, timeout: int = 120):
    logger.info(f"Waiting for {type}")
    template = cv2.imread(type.value, cv2.IMREAD_GRAYSCALE)

    # Crash detection
    relaunchButton = cv2.imread(Button.RELAUNCH.value, cv2.IMREAD_GRAYSCALE)

    # Idle detection
    keepPlayingButton = cv2.imread(Button.KEEP_PLAYING.value, cv2.IMREAD_GRAYSCALE)

    startTime = now()

    while True and now() - startTime < timeout:
        frame = self.grab()

        if frame is None:
          continue

        position = self.find(frame, template)

        relaunchButtonPos = self.find(frame, relaunchButton)
        if relaunchButtonPos:
          logger.info('Crash detected')
          return None, relaunchButtonPos, None

        keepPlayingButtonPos = self.find(frame, keepPlayingButton)
        if keepPlayingButtonPos:
          logger.info('KeepPlaying detected')
          return None, None, keepPlayingButtonPos

        if position:
          logger.info(f'Step {type} found')
          return position, False, False

        sleep(2)

    logger.info(f"waitFor() - {timeout}s timeout")
    return None, None, None
