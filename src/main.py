import cv2
from controls import Controls
from gamemode.drive import Drive
from enums import Button, Text
from playbook import PLAYBOOK_DRIVE
import utils


controls = Controls()
drive = Drive()

def main():

  # configs = utils.readConfig()
  # gamemode = utils.waitForGamemode(configs)

  drive.start()

  # for step in PLAYBOOK_DRIVE:
  #   position = utils.waitFor(step)

  #   if step == Button.HOLD_START:
  #     controls.hold('enter', 5)

  #   elif step == Button.DRIVE_CAR:
  #     controls.hold('e', 5)
  #   else:
  #     controls.click((position[0] + position[2])//2 , (position[1] + position[3])//2)

  # controls.scrollDown()


if __name__ == '__main__':
     main()
