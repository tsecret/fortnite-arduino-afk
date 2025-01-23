import threading
import json
from time import sleep

from utils import logger
from config import config

if config.isWindows():
  import win32api, win32con
  import pydirectinput

if config.isMac():
  import pyautogui as pydirectinput


class Controls:

  def click(self, x: int, y: int) -> None:
    logger.info(f'Clicking on [{x} {y}]')
    pydirectinput.click(x, y, duration=0.5)

  def holdLeftMouse(self, duration: int):
    pydirectinput.mouseDown(None, None, pydirectinput.MOUSE_LEFT)
    sleep(duration)
    pydirectinput.mouseDown(None, None, pydirectinput.MOUSE_LEFT)

  def scrollDown(self) -> None:
    logger.info('Scrolling down')
    pydirectinput.scroll(-10)

  def press(self, key, duration):
    pydirectinput.keyDown(key)
    sleep(duration)
    pydirectinput.keyUp(key)

  def hold(self, key: str, duration: int):
    threading.Thread(target=self.press, args=(key, duration)).start()

  def left(self):
    pydirectinput.press('a')

  def right(self):
    pydirectinput.press('d')

  def moveMouse(self, x: int, y: int):
    if config.isWindows():
      win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x), int(y), 0,0)

    sleep(0.5)

  def playSequence(self, name: str):
    with open(name, 'r') as f:
      actions = json.load(f)

    t = actions[0]['time']

    for i, action in enumerate(actions):

      sleep_time = action['time'] - t
      logger.info(f"Sleeping for {sleep_time}s")

      if sleep_time > 0:
        sleep(sleep_time)

      logger.info(f"Action {action['action']}; {action['key']}; duration {action['duration']}")

      if action['action'] == 'key':
        pydirectinput.press(action['key'], duration=action['duration'])

      if action['action'] == 'mouse_move':
        pydirectinput.moveRel(action['x'], action['y'], disable_mouse_acceleration=True, relative=True)

      t = action['time'] + action['duration'] if 'duration' in action else 0
