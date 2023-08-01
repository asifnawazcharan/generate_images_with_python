import cv2
import random
import numpy as np
import os

def generate_image(number, background_color, font_color):
  image = np.zeros((500, 500, 3), dtype=np.uint8)
  image[:] = background_color
  cv2.putText(image, str(number), (int(image.shape[1] / 2), int(image.shape[0] / 2)), cv2.FONT_HERSHEY_SIMPLEX, 5, font_color, 5, lineType=cv2.LINE_AA)
  return image

def save_image(image, filename):
  if not os.path.exists("images"):
    os.mkdir("images")
  path = os.path.join("images", filename)
  cv2.imwrite(path, image)

def generate_contrasting_color(background_color):
  """Returns a contrasting font color for the given background color."""
  brightness = (background_color[0] + background_color[1] + background_color[2]) / 3
  if brightness < 128:
    return (255, 255, 255)  # white
  else:
    return (0, 0, 0)  # black

for number in range(51):
  background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  font_color = generate_contrasting_color(background_color)
  image = generate_image(number, background_color, font_color)
  filename = f"image_{number}.png"
  save_image(image, filename)
  print("One down!")
