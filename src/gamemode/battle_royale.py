from playbook import PLAYBOOK_BR_RELOADED, PLAYBOOK_LEAVE_BR_RELOADED
from time import sleep, time as now
from random import randint
from utils import logger
from gamemode.gamemodeBase import GamemodeBase

class BattleRoyale(GamemodeBase):

  def start(self):
    self.executePlaybook(PLAYBOOK_BR_RELOADED)
    sleep(5)
    self.leave()

  def idle(self):
    IDLE_TIME = int(15 * 60 + 60)
    MOVE_TIME = int(1 * 60)

    start_time = now()
    last_move_time = now()

    while now() - start_time <= IDLE_TIME:
      logger.info(f"Idle ends in {IDLE_TIME - int(now() - start_time)}s. Moving in {IDLE_TIME - int(now()-last_move_time)}s", end='\r')

      if now() - last_move_time >= MOVE_TIME:
        logger.info(f"Moving", end='\r')
        self.controls.press('w', randint(1, 5))
        self.controls.press('s', randint(1, 5))

        last_move_time = now()

      sleep(1)

    self.checkExp()

  def leave(self):
    self.controls.press('esc', 0.5)
    self.executePlaybook(PLAYBOOK_LEAVE_BR_RELOADED)
    self.controls.scrollDown()
