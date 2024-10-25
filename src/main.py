import numpy as np
from PIL import ImageGrab
import cv2

def getImage():
      frame = np.array(ImageGrab.grab(bbox=(0, 0, 800, 600)))
      frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
      return frame

def capture_screen():
    while True:


        # cv2.imshow('Screen Capture', screen)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def main():
  frame = getImage()
  print(frame)

if __name__ == '__main__':
     main()
