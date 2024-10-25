import cv2
from time import sleep
from detector import Detector
from mouse import Mouse
from enums import Button, Text
from playbook import PLAYBOOK_FESTIVAL, PLAYBOOK_LEAVE_FESTIVAL

WIDTH = 1920
HEIGHT = 1080

detector = Detector()
mouse = Mouse()

def waitFor(type: Button | Text):

  print(f"Waiting for {type}")
  template = cv2.imread(type.value, cv2.IMREAD_GRAYSCALE)

  while True:
      frame = detector.getImage(WIDTH, HEIGHT)
      position = detector.find(frame, template)

      if position:
        print(f'Step {type} found')
        return position

      sleep(2)


def main():
  for step in PLAYBOOK_FESTIVAL:
    position = waitFor(step)
    mouse.click((position[0] + position[2])//2 , (position[1] + position[3])//2)

  mouse.scrollDown()


if __name__ == '__main__':
     main()
