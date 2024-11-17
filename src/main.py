from controls import Controls
from gamemode.lego import Lego
from gamemode.tttycoon import TikTokTycoon
from gamemode.battle_royale import BattleRoyale
from enums import Gamemode

controls = Controls()

def main():
  while True:
    # configs = utils.readConfig()
    # gamemode = utils.waitForGamemode(configs)
    gamemode = Gamemode.BR_RELOAD

    tycoon = TikTokTycoon()
    tycoon.start()

    tycoon = TikTokTycoon()
    tycoon.start()

    br = BattleRoyale()
    br.start()

    # if gamemode == Gamemode.LEGO:
    #   lego = Lego()
    #   lego.start()

    # if gamemode == Gamemode.TYCOON:
    #   tycoon = TikTokTycoon()
    #   tycoon.start()

    # if gamemode == Gamemode.BR_RELOAD:
    #   br = BattleRoyale()
    #   br.start()

if __name__ == '__main__':
     main()
