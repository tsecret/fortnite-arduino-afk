from gamemode.tttycoon import TikTokTycoon
from gamemode.battle_royale import BattleRoyale
from gamemode.lego import Lego

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

def main():

  model = ocr_predictor(pretrained=True)
  doc = DocumentFile.from_images("./xp.png")

  result = model(doc)
  print(result.pages[0].blocks[0])

  # tycoon = Lego()
  # tycoon.checkExp()

  # while True:

    # tycoon = TikTokTycoon()
    # tycoon.start()

    # tycoon = TikTokTycoon()
    # tycoon.start()

    # br = BattleRoyale()
    # br.start()

    # lego = Lego()
    # lego.start()

  pass

if __name__ == '__main__':
     main()
