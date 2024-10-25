import pyautogui

class Mouse:
  def click(self, x: int, y: int) -> None:
    print(f'Clicking on [{x} {y}]')
    pyautogui.click(x, y, duration=1)

  def press(self, key: str) -> None:
    print(f"Pressing {key}")
    pyautogui.press(key)

  def scrollDown(self) -> None:
    pyautogui.scroll(-10)
