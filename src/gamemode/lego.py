from playbook import PLAYBOOK_LEGO, PLAYBOOK_LEAVE_LEGO
from enums import Button, Text
import utils
from controls import Controls
from time import sleep, time as now
from random import randint
from gamemode.gamemodeBase import GamemodeBase

class Lego(GamemodeBase):

  def start(self):
    self.executePlaybook(PLAYBOOK_LEGO)

  def leave(self):
    self.controls.press('esc', 0.5)
    self.executePlaybook(PLAYBOOK_LEAVE_LEGO)
    sleep(2)
    self.controls.scrollDown()

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

    self.leave()
