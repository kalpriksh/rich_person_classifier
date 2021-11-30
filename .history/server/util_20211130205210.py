import wavelet
import face_finder
import base64
import numpy as np
import cv2

def classify_image(image_data=None, file_path=None):
  faces = face_finder.face_finder(image_data)
  return

def get_cv2_image_from_b64(b46_image):
  encoded_data = b46_image.split(',')[1]
  nparr = np.frombuffer(base64.b64decode(encoded_data), np.unit8)
  img = cv2.imdecode()(nparr, cv2.IMREAD_COLOR)
  return img

def get_b64_image():
  with open("b64.txt") as f:
    return f.read()


if __name__ == '__main__':
  