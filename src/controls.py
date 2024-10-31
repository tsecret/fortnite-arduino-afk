import pyautogui
from time import sleep
import threading

class Controls:
  def click(self, x: int, y: int) -> None:
    print(f'Clicking on [{x} {y}]')
    pyautogui.click(x, y, duration=1)

  def press(self, key: str) -> None:
    print(f"Pressing {key}")
    pyautogui.press(key)

  def scrollDown(self) -> None:
    pyautogui.scroll(-10)

  def press(self, key, duration):
      pyautogui.keyDown(key)
      sleep(duration)
      pyautogui.keyUp(key)

  def hold(self, key: str, duration: int):
    threading.Thread(target=self.press, args=(key, duration)).start()

  def left(self):
    pyautogui.press('a')

  def right(self):
    pyautogui.press('d')
