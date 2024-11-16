from playbook import PLAYBOOK_BR_RELOADED, PLAYBOOK_LEAVE_BR_RELOADED
from camera import Camera
from controls import Controls
from enums import Button, Text
from time import sleep, time as now
import re
import easyocr
from random import randint

class BattleRoyale:
  camera = None
  controls = None

  ocr = easyocr.Reader(['en'], gpu=False)

  lvlStart: int = None
  lvl: int = None

  prevExp: int = None
  exp: int = None

  def __init__(self):
    self.camera = Camera()
    self.controls = Controls()

  def start(self):

    for step in PLAYBOOK_BR_RELOADED:
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

    self.checkExp()
    sleep(5)

    self.leave()

    # self.controls.press('space', 0.5)

    # self.idle()

  def idle(self):
    IDLE_TIME = int(15 * 60 + 60)
    MOVE_TIME = int(1 * 60)

    start_time = now()
    last_move_time = now()

    while now() - start_time <= IDLE_TIME:
      print(f"Idle ends in {IDLE_TIME - int(now() - start_time)}s. Moving in {IDLE_TIME - int(now()-last_move_time)}s", end='\r')

      if now() - last_move_time >= MOVE_TIME:
        print(f"Moving", end='\r')
        self.controls.press('w', randint(1, 5))
        self.controls.press('s', randint(1, 5))

        last_move_time = now()

      sleep(1)

    self.checkExp()

  def leave(self):
    self.controls.press('esc', 0.5)

    for step in PLAYBOOK_LEAVE_BR_RELOADED:
      position, crashPos, idlePos = self.camera.waitFor(step)

      if position:

        if step.value in [e.value for e in Text]:
          continue

        else:
          self.controls.click(position[0], position[1])

    self.controls.scrollDown()

  def checkExp(self) -> bool:
    REGEX = r"LVL\s?(\d+)\s+([\d,]+)\s?XP to LVL (\d+)"

    self.prevExp = self.exp

    self.controls.press('esc', 0.5)

    while True:

      frame = self.camera.grab((480, 635, 800, 675))

      result = self.ocr.readtext(frame, detail=0)
      print(f"Result from OCR: {result}")

      if len(result) < 2:
        print("Incorrect checkExp reading")
        return

      result = " ".join(result)

      response = re.findall(REGEX, result, re.MULTILINE)
      print(f"Result from response: {response}")

      if len(response) > 0:
        parsedResult = response[0]
        print(f'Result from regex: {parsedResult}')

        self.lvl = int(parsedResult[0])
        if self.lvlStart is None: self.lvlStart = self.lvl

        self.exp = 80_000 - int(parsedResult[1].replace(',',''))
        if self.prevExp is None: self.prevExp = self.exp

        break

      print(f"EXP read did not succeed, trying again")

    print(f"Level: {self.lvlStart} -> {self.lvl}. Remaining exp {self.prevExp or 0} -> {self.exp}")

    self.controls.press('esc', 0.5)
