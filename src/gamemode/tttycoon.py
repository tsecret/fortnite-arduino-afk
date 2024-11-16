import easyocr
from controls import Controls
from camera import Camera
import re
from playbook import PLAYBOOK_TTTYCOON, PLAYBOOK_LEAVE_TTTYCOON
from enums import Button, Text
from time import sleep
import logging

class TikTokTycoon:
  controls = Controls()
  camera = Camera()
  ocr = easyocr.Reader(['en'], gpu=False)

  lvlStart: int = None
  lvl: int = None

  prevExp: int = None
  exp: int = None

  def __init__(self):
    pass

  def start(self):
    # Loads the map
    for step in PLAYBOOK_TTTYCOON:
      position, crashPos, idlePos = self.camera.waitFor(step)

      if idlePos:
        self.controls.click(idlePos[0], idlePos[1])

      if position:

        if step.value in [e.value for e in Text]:
          continue

        elif step == Button.HOLD_START:
          self.controls.hold('enter', 3)

        else:
          self.controls.click(position[0], position[1])

    sleep(15)

    # Action script
    self.controls.playSequence('./scripts/tttycon.json')

    self.controls.moveMouse(0, 3000)

    self.idle()

  def leave(self):
    self.controls.press('esc', 0.5)

    for step in PLAYBOOK_LEAVE_TTTYCOON:
      position, crashPos, idlePos = self.camera.waitFor(step)

      if position:

        if step.value in [e.value for e in Text]:
          continue

        else:
          self.controls.click(position[0], position[1])

    self.controls.scrollDown()

  def idle(self):
    self.checkExp()

    shootDuration = 30

    while True:
      self.controls.holdLeftMouse(shootDuration)
      self.checkExp()

      if self.prevExp == self.exp:
        logging.info('No xp gain')
        break

    self.leave()

  def checkExp(self) -> bool:
    REGEX = r"LVL\s?(\d+)\s+([\d,]+)\s?XP to LVL (\d+)"

    self.prevExp = self.exp

    self.controls.press('esc', 0.5)

    while True:

      frame = self.camera.grab((480, 635, 800, 675))

      result = self.ocr.readtext(frame, detail=0)
      logging.info(f"Result from OCR: {result}")

      if len(result) < 2:
        logging.info("Incorrect checkExp reading")
        return

      result = " ".join(result)

      response = re.findall(REGEX, result, re.MULTILINE)
      logging.info(f"Result from response: {response}")

      if len(response) > 0:
        parsedResult = response[0]
        logging.info(f'Result from regex: {parsedResult}')

        self.lvl = int(parsedResult[0])
        if self.lvlStart is None: self.lvlStart = self.lvl

        self.exp = 80_000 - int(parsedResult[1].replace(',',''))
        if self.prevExp is None: self.prevExp = self.exp

        break

      logging.info(f"EXP read did not succeed, trying again")

    logging.info(f"Level: {self.lvlStart} -> {self.lvl}. Remaining exp {self.prevExp or 0} -> {self.exp}")

    self.controls.press('esc', 0.5)
