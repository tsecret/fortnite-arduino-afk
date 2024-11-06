from controls import Controls
from gamemode.lego import Lego
from enums import Gamemode
import utils

controls = Controls()

def main():
    configs = utils.readConfig()
    gamemode = utils.waitForGamemode(configs)
    # gamemode = Gamemode.LEGO

    if gamemode == Gamemode.LEGO:
      lego = Lego()
      lego.start()

if __name__ == '__main__':
     main()
