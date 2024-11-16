import pydirectinput
from time import sleep
import threading
import win32api, win32con
import json

class Controls:

  def click(self, x: int, y: int) -> None:
    print(f'Clicking on [{x} {y}]')
    pydirectinput.click(x, y, duration=1)

  def holdLeftMouse(self, duration: int):
    pydirectinput.mouseDown(None, None, pydirectinput.MOUSE_LEFT)
    sleep(duration)
    pydirectinput.mouseDown(None, None, pydirectinput.MOUSE_LEFT)

  def scrollDown(self) -> None:
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
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x), int(y), 0,0)
    sleep(0.5)

  def playSequence(self, name: str):
    with open(name, 'r') as f:
      actions = json.load(f)

    t = actions[0]['time']

    for i, action in enumerate(actions):

      sleep_time = action['time'] - t
      print('sleep', sleep_time)

      if sleep_time > 0:
        sleep(sleep_time)

      print(action)

      if action['action'] == 'key':
        pydirectinput.press(action['key'], duration=action['duration'])

      if action['action'] == 'mouse_move':
        pydirectinput.moveRel(action['x'], action['y'], disable_mouse_acceleration=True, relative=True)

      t = action['time'] + action['duration'] if 'duration' in action else 0
