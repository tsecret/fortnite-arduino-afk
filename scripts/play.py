import pydirectinput
import json
from time import sleep

with open('./scripts/records.json', 'r') as f:
  actions = json.load(f)

print(f"Loaded {len(actions)} actions")

sleep(2)

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
