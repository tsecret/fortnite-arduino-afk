import cv2
from detector import Detector
from controls import Controls
import numpy as np
from enum import Enum
from time import time

class Mode(Enum):
  FORWARD = 1
  BACKWARD = 2

class Drive():
  detector: Detector
  controls: Controls
  MODE: Mode = Mode.FORWARD
  TOP_POS = 400
  BOT_POS = 550

  def __init__(self):
    self.detector = Detector()
    self.controls = Controls()

  def average_horizontal_position(self, lines) -> int | None:
    horizontal_lines = []

    for line in lines:
      for x1, y1, x2, y2 in line:
        if x1 == x2:
          continue

        slope = (y2 - y1) / (x2 - x1)



        if -0.5 < slope < 0.5:
          horizontal_lines.append((y1 + y2) // 2)

    if len(horizontal_lines):
      return sum(horizontal_lines) // len(horizontal_lines)

    return None

  def region_selection(self, image):
    """
    Determine and cut the region of interest in the input image.
    Parameters:
      image: we pass here the output from canny where we have
      identified edges in the frame
    """
    # create an array of the same size as of the input image
    mask = np.zeros_like(image)
    # if you pass an image with more then one channel
    if len(image.shape) > 2:
      channel_count = image.shape[2]
      ignore_mask_color = (255,) * channel_count
    # our image only has one channel so it will go under "else"
    else:
      # color of the mask polygon (white)
      ignore_mask_color = 255
    # creating a polygon to focus only on the road in the picture
    # we have created this polygon in accordance to how the camera was placed

    X_OFFSET_TOP = 150
    X_OFFSET_BOT = 400
    Y_OFFSET = 500
    X_MID = image.shape[1] // 2
    Y_MAX = image.shape[0]


    rows, cols = image.shape[:2]
    bottom_left = [X_MID - X_OFFSET_BOT, Y_MAX]
    top_left   = [X_MID - X_OFFSET_TOP, Y_MAX - Y_OFFSET]
    bottom_right = [X_MID + X_OFFSET_BOT, Y_MAX]
    top_right  = [X_MID + X_OFFSET_TOP, Y_MAX - Y_OFFSET]


    vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

  def start(self):
    WINDOW_NAME = 'Game'

    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, self.detector.WIDTH // 2, self.detector.HEIGHT // 2)
    cv2.moveWindow(WINDOW_NAME, self.detector.WIDTH, 0)

    kernel_size = 5

    # (hMin = 0 , sMin = 0, vMin = 216), (hMax = 179 , sMax = 27, vMax = 255)

    last_gas = time()

    while True:
      frame = self.detector.getImage(color=cv2.COLOR_BGR2HSV)
      frame = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)

      originalFrame = frame.copy()
      originalFrame = cv2.cvtColor(originalFrame, cv2.COLOR_HSV2RGB)

      hsv_color1 = np.asarray([0, 0, 216])
      hsv_color2 = np.asarray([179, 27, 255])

      frame = cv2.inRange(frame, hsv_color1, hsv_color2)
      frame = self.region_selection(frame)

      frame = cv2.Canny(frame, 50, 150)

      lines = cv2.HoughLinesP(frame, 10, np.pi / 2, threshold=15, minLineLength=100, maxLineGap=20)


      if lines is not None:
        y = self.average_horizontal_position(lines)

        if y is not None:
          if y > self.BOT_POS and self.MODE == Mode.FORWARD:
            self.MODE = Mode.BACKWARD
            print('Switched to BACK')

          if y < self.TOP_POS and self.MODE == Mode.BACKWARD:
            self.MODE = Mode.FORWARD
            print('Switched to FORW')

          cv2.line(originalFrame, (0, y), (self.detector.WIDTH, y), (0, 0, 255), 3)

        cv2.line(originalFrame, (0, self.TOP_POS), (self.detector.WIDTH, self.TOP_POS), (0, 0, 255), 3)
        cv2.line(originalFrame, (0, self.BOT_POS), (self.detector.WIDTH, self.BOT_POS), (0, 0, 255), 3)

      if time() - last_gas >= 1:
        if self.MODE == Mode.FORWARD:
          self.controls.hold('w', 0.0001)
          last_gas = time()
        else:
          self.controls.hold('s', 0.0001)
          last_gas = time()



      cv2.imshow(WINDOW_NAME, originalFrame)

      if cv2.waitKey(25) & 0xFF == ord('q'):
        break
