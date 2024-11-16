from controls import Controls
from gamemode.lego import Lego
from gamemode.tttycoon import TikTokTycoon
from enums import Gamemode

controls = Controls()

def main():
  while True:
    # configs = utils.readConfig()
    # gamemode = utils.waitForGamemode(configs)
    gamemode = Gamemode.TYCOON

    if gamemode == Gamemode.LEGO:
      lego = Lego()
      lego.start()

    if gamemode == Gamemode.TYCOON:
      tycoon = TikTokTycoon()
      tycoon.start()

if __name__ == '__main__':
     main()
