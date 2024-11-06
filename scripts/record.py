from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Key
from time import sleep, time as now
import json
import sys

actions = []
buttons = {}

sleep(2)
print("Recording")

def on_press(key):
  if key == Key.esc:
    with open('./scripts/records.json', 'w') as f:
      json.dump(actions, f)

    return False

  if key.char not in buttons:
    print(f"Pressed {key}")
    buttons[key.char] = now()

def on_release(key):
  print(f"Released {key}")

  key = key.char

  print(buttons)
  actions.append({ 'action': 'key', 'key': key, 'time': buttons[key], "duration": now() - buttons[key] })

  del buttons[key]

def on_move(x, y):
  print(f"Moved to ({x};{y})")
  action = {'action':'mouse_move', "x": x, "y": y, 'time': now()}
  actions.append(action)

def on_click(x, y, button, pressed):
  if button == Button.middle:
    with open('./scripts/records.json', 'w') as f:
      json.dump(actions, f)

    return False

  print(f"Clicked on ({x};{y}) with {button}, pressed {pressed}")
  action = {'action':'mouse_click', "x": x, "y": y, "button": button, 'time': now()}
  actions.append(action)

keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

# mouse_listener = mouse.Listener(
#     on_click=on_click,
#     on_move=on_move)

keyboard_listener.start()
# mouse_listener.start()
keyboard_listener.join()
# mouse_listener.join()
