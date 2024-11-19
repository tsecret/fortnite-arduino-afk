from gamemode.tttycoon import TikTokTycoon
from gamemode.battle_royale import BattleRoyale

def main():
  while True:

    tycoon = TikTokTycoon()
    tycoon.start()

    tycoon = TikTokTycoon()
    tycoon.start()

    br = BattleRoyale()
    br.start()

if __name__ == '__main__':
     main()
