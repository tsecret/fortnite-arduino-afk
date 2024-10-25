import cv2

def drawBox(frame, pos1, pos2):
  return cv2.rectangle(frame, pos1, pos2, (255, 255, 255), 2)
