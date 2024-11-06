import dxcam

class Camera:
  WIDTH = 1920
  HEIGHT = 1080
  REGION = (0, 0, WIDTH, HEIGHT)

  camera = None

  def __init__(self) -> None:
    self.camera = dxcam.create(output_color='RGB', output_idx=0)

  def grab(self):
    return self.camera.grab(self.REGION)
