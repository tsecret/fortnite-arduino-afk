import cv2
import numpy as np
from typing import Tuple, List
from PIL import ImageGrab

class Detector:
  THRESHOLD = 0.8

  def __init__(self) -> None:
    pass

  def _matchTemplate(self, frame, template):
    res = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
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

  def getImage(self, width, height):
    frame = np.array(ImageGrab.grab(bbox=(0, 0, width, height)))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame
