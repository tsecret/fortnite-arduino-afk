from utils import logger
from time import sleep
from controls import Controls
from camera import camera
import re
from enums import Button, Text, WaitForResults

class GamemodeBase:
  controls = Controls()


  lvlStart: int = None
  lvl: int = None

  prevExp: int = None
  exp: int = None

  def __init__(self):
    pass

  def executePlaybook(self, playbook) -> None:
    for step in playbook:
      type, position = camera.waitFor(step)

      # Intermetiate screens like Claim Stars Button, Sleep Button, Crash, etc
      # Just click them and execute waitFor again for the same step
      if type == WaitForResults.CLAIM:
        self.controls.click(position[0], position[1])
        sleep(5)
        type, position = camera.waitFor(step)

      # All good, continue to next step
      if type == WaitForResults.POSITION:

        if step.value in [e.value for e in Text]:
          continue

        elif step == Button.HOLD_START:
          self.controls.hold('enter', 3)

        else:
          self.controls.click(position[0], position[1])
          sleep(2)

      # Image was not found within the given interval
      if type is None:
        continue

  def end(self) -> None:
    pass

  def idle(self) -> None:
    pass

  def checkExp(self) -> bool:
    REGEX = r"\d+(?:,\d+)?"

    self.prevExp = self.exp

    self.controls.press('esc', 0.5)

    frame = camera.grab((480, 635, 800, 675))

    if frame is None:
      self.controls.press('esc', 0.5)
      sleep(2)
      return self.checkExp()

    result = camera.readText(frame)
    logger.info(f"Result from OCR: {result}")

    if len(result) < 2:
      logger.info("Incorrect checkExp reading")
      self.controls.press('esc', 0.5)
      sleep(2)
      return self.checkExp()

    result = " ".join(result)

    regexResult = re.findall(REGEX, result, re.MULTILINE)
    print(f"Regex result: {regexResult}")

    self.lvl = int(regexResult[0])
    if self.lvlStart is None: self.lvlStart = self.lvl

    self.exp = 80_000 - int(regexResult[1].replace(',',''))
    if self.prevExp is None: self.prevExp = self.exp

    logger.info(f"Level: {self.lvlStart} -> {self.lvl}. Remaining exp {self.prevExp or 0} -> {self.exp}")

    self.controls.press('esc', 0.5)
