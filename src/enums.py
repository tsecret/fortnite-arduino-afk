from enum import Enum

ASSETS_BASE = './assets/'

class Button(Enum):
  LIBRARY = ASSETS_BASE + 'buttonGamemodeLibrary.png'
  RANKED = ASSETS_BASE + 'buttonGamemodeRanked.png'
  FESTIVAL = ASSETS_BASE + 'buttonGamemodeFestival.png'
  LEGO = ASSETS_BASE + 'buttonGamemodeLego.png'
  PLAY = ASSETS_BASE + 'buttonPlay.png'
  PLAY_LEGO = ASSETS_BASE + 'buttonPlayLego.png'
  NO_FILL = ASSETS_BASE + 'buttonNoFill.png'
  SELECT = ASSETS_BASE + 'buttonSelect.png'
  SELECT_WORLD = ASSETS_BASE + 'buttonSelectWorld.png'
  YES = ASSETS_BASE + 'buttonYes.png'
  RETURN_TO_LOBBY = ASSETS_BASE + 'buttonReturnToLobby.png'
  LEAVE = ASSETS_BASE + 'buttonLeave.png'


class Text(Enum):
  CHOOSE_SONG = ASSETS_BASE + 'textChooseSong.png'
  FESTIVAL = ASSETS_BASE + 'textFestival.png'
  WORLD_NAME = ASSETS_BASE + 'textWorldName.png'
  BUILD = ASSETS_BASE + 'textBuild.png'
  LEGO = ASSETS_BASE + 'textLego.png'
