from enums import Button, Text, Gamemode
import cv2
from detector import Detector
from time import sleep, time as now
import json
from typing import List, Dict
from datetime import datetime

detector = Detector()

type Config = Dict[str, str, str]

def readConfig() -> List[Config]:
   with open('./config.json', 'r') as config:
      print("Reading config")
      return json.load(config)

def waitForGamemode(configs: List[Config]) -> Gamemode:
  assert len(configs), 'Config list is empty'

  now = datetime.now().timestamp()

  nextGamemode: Gamemode = None
  nextGamemodeTime: datetime = None
  for config in configs:
    tFestival = datetime.strptime(config['festival'], "%H:%M").replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day).timestamp()
    tLego = datetime.strptime(config['lego'], "%H:%M").replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day).timestamp()

    if abs(tFestival - now) < abs(tLego - now):
       nextGamemode = Gamemode.FESTIVAL
       nextGamemodeTime = tFestival
    else:
       nextGamemode = Gamemode.LEGO
       nextGamemodeTime = tLego

  while datetime.now().timestamp() < nextGamemodeTime:
     print(f"Waiting for gamemode {nextGamemode.value} in {int((nextGamemodeTime - datetime.now().timestamp()))}s", end='\r', flush=True)
     sleep(1)

  return nextGamemode

def waitFor(type: Button | Text, timeout: int = 120):

  print(f"Waiting for {type}")
  template = cv2.imread(type.value, cv2.IMREAD_GRAYSCALE)

  # Crash detection
  relaunchButton = cv2.imread(Button.RELAUNCH.value, cv2.IMREAD_GRAYSCALE)

  # Idle detection
  keepPlayingButton = cv2.imread(Button.KEEP_PLAYING.value, cv2.IMREAD_GRAYSCALE)

  startTime = now()

  while True and now() - startTime < timeout:
      frame = detector.getImage()
      position = detector.find(frame, template)

      relaunchButtonPos = detector.find(frame, relaunchButton)
      if relaunchButtonPos:
         print('Crash detected')
         return None, relaunchButtonPos, None

      keepPlayingButtonPos = detector.find(frame, keepPlayingButton)
      if keepPlayingButtonPos:
         print('KeepPlaying detected')
         return None, None, keepPlayingButtonPos

      if position:
        print(f'Step {type} found')
        return position, False, False

      sleep(2)

  print(f"waitFor() - {timeout}s timeout")
  return None, None, None
