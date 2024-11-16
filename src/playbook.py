from enums import Button, Text

PLAYBOOK_FESTIVAL = [
  Button.LIBRARY,
  Button.FESTIVAL,
  Button.SELECT,
  Text.FESTIVAL,
  Button.PLAY,
  Text.CHOOSE_SONG
]

PLAYBOOK_LEGO = [
  Button.LIBRARY,
  Button.LEGO,
  Button.SELECT,
  Button.SELECT_WORLD,
  Text.WORLD_NAME,
  Button.PLAY_LEGO,
]

PLAYBOOK_DRIVE = [
  # Button.LIBRARY,
  # Button.DRIVE,
  # Button.SELECT,
  # Text.DRIVE,
  # Button.PLAY,
  Button.HOLD_START,
  Button.DRIVE_CAR,
  Text.SPEED
]

PLAYBOOK_LEAVE_FESTIVAL = [
  Button.LEAVE,
  Button.RETURN_TO_LOBBY,
  Button.YES,
  Text.FESTIVAL,
]

PLAYBOOK_LEAVE_LEGO = [
  Button.LEAVE,
  Button.RETURN_TO_LOBBY,
  Button.YES,
  Text.LEGO,
]

PLAYBOOK_TTTYCOON = [
  Button.LIBRARY,
  Button.TTTYCOON,
  Button.SELECT,
  Text.TTTYCOON,
  Button.PLAY,
  Button.HOLD_START,
  # Text.TTTYCOON_STARTED
]

PLAYBOOK_LEAVE_TTTYCOON = [
  Button.LEAVE,
  Button.RETURN_TO_LOBBY,
  Button.YES,
  Text.TTTYCOON,
]
