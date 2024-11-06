from playbook import PLAYBOOK_LEGO, PLAYBOOK_LEAVE_LEGO
from enums import Button, Text
import utils
from controls import Controls
from time import sleep, time as now
from random import randint

class Lego:
  def __init__(self):
    self.controls = Controls()

  def start(self):
    print('Starting LEGO playbook')

    for step in PLAYBOOK_LEGO:
      position, crashPos, idlePos = utils.waitFor(step)

      if idlePos:
        self.controls.click(idlePos[0], idlePos[1])

      if position:
        self.controls.click(position[0], position[1])

    self.idle()

  def idle(self):
    IDLE_TIME = int(2.5 * 60 * 60) + 60
    MIN_JUMPS = 2
    MAX_JUMPS = 10

    startTime = now()
    lastMoveTime = now()
    afkInterval = 10 * 60

    print(f"Starting Lego idle for {IDLE_TIME} seconds")

    while now() - startTime <= IDLE_TIME:
      print(f"Idle ends in {IDLE_TIME - int(now() - startTime)}s. Moving in {afkInterval - int(now()-lastMoveTime)}s", end='\r')

      if now() - lastMoveTime >= afkInterval:
        print(f"Moving", end='\r')
        self.controls.press('w', randint(MIN_JUMPS, MAX_JUMPS))
        self.controls.press('s', randint(MIN_JUMPS, MAX_JUMPS))

        lastMoveTime = now()

      sleep(1)


  def end(self):
    pass
