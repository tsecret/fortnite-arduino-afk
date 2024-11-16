from enums import Gamemode
from time import sleep
import json
from typing import List, Dict
from datetime import datetime

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
