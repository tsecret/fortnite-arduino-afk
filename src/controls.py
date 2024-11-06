import pydirectinput
from time import sleep
import threading
import win32api, win32con

class Controls:

  def click(self, x: int, y: int) -> None:
    print(f'Clicking on [{x} {y}]')
    pydirectinput.click(x, y, duration=1)

  def press(self, key: str) -> None:
    print(f"Pressing {key}")
    pydirectinput.press(key)

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
