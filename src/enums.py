from enum import Enum

ASSETS_BASE = './assets/'

class Button(Enum):
  # UI
  LIBRARY = ASSETS_BASE + 'buttonGamemodeLibrary.png'
  PLAY = ASSETS_BASE + 'buttonPlay.png'
  NO_FILL = ASSETS_BASE + 'buttonNoFill.png'
  SELECT = ASSETS_BASE + 'buttonSelect.png'
  YES = ASSETS_BASE + 'buttonYes.png'
  RETURN_TO_LOBBY = ASSETS_BASE + 'buttonReturnToLobby.png'
  LEAVE = ASSETS_BASE + 'buttonLeave.png'
  RELAUNCH = ASSETS_BASE + 'buttonRelaunch.png'
  HOLD_START = ASSETS_BASE + 'buttonHoldStart.png' #hold
  KEEP_PLAYING = ASSETS_BASE + 'buttonKeepPlaying.png' # keep checking

  # Festival
  FESTIVAL = ASSETS_BASE + 'buttonGamemodeFestival.png'

  # Lego
  LEGO = ASSETS_BASE + 'buttonGamemodeLego.png'
  PLAY_LEGO = ASSETS_BASE + 'buttonPlayLego.png'
  SELECT_WORLD = ASSETS_BASE + 'buttonSelectWorld.png'

  # Drive
  DRIVE = ASSETS_BASE + 'buttonGamemodeDrive.png'
  DRIVE_CAR = ASSETS_BASE + 'buttonDrive.png' #hold

  # TTTycoon
  TTTYCOON = ASSETS_BASE + 'buttonGamemodeTTTycoon.png'

class Text(Enum):
  CHOOSE_SONG = ASSETS_BASE + 'textChooseSong.png'
  FESTIVAL = ASSETS_BASE + 'textFestival.png'
  WORLD_NAME = ASSETS_BASE + 'textWorldName.png'
  BUILD = ASSETS_BASE + 'textBuild.png'
  LEGO = ASSETS_BASE + 'textLego.png'

  # Drive
  DRIVE = ASSETS_BASE + 'textDrive.png'
  SPEED = ASSETS_BASE + 'textSpeed.png'

  # TTTycoon
  TTTYCOON = ASSETS_BASE + 'textTTTycoon.png'
  TTTYCOON_STARTED = ASSETS_BASE + 'textTTTycoonStarted.png'

class Gamemode(Enum):
  FESTIVAL = 'FESTIVAL'
  LEGO = 'LEGO'
  DRIVE = 'DRIVE'
  TYCOON = 'TYCOON'
