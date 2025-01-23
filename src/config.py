from sys import platform

class Config:

  def isWindows(self):
    return platform == 'win32'

  def isMac(self):
    return platform == 'darwin'

config = Config()
