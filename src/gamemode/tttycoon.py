from playbook import PLAYBOOK_TTTYCOON, PLAYBOOK_LEAVE_TTTYCOON
from time import sleep
from utils import logger
from gamemode.gamemodeBase import GamemodeBase

class TikTokTycoon(GamemodeBase):

  def start(self):
    # Loads the map
    self.executePlaybook(PLAYBOOK_TTTYCOON)

    sleep(20)

    # Action script
    self.controls.playSequence('./scripts/tttycon.json')

    self.controls.moveMouse(0, 3000)

    self.idle()

  def leave(self):
    self.controls.press('esc', 0.5)
    self.executePlaybook(PLAYBOOK_LEAVE_TTTYCOON)
    self.controls.scrollDown()

  def idle(self):
    SHOOT_DURATION = 30

    self.checkExp()

    while True:
      self.controls.holdLeftMouse(SHOOT_DURATION)
      self.checkExp()

      if self.prevExp == self.exp:
        logger.info('No xp gain')
        break

    self.leave()
