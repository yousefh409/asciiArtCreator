import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt

######## CONSTANTS ########
image_name = "../content/sample_data/liverpoolLogo.png"
ascii_max_x = 40
ascii_max_y = 40
threshold = 127
art_char = "█"
######## ######### ########

image_name = "../content/sample_data/liverpoolLogo.png"
img = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)


_, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

img = cv2.resize(img, (ascii_max_x, ascii_max_y)) 

result = ""
for i in range(ascii_max_x):
  for j in range(ascii_max_y):
    if img[(i, j)] > threshold:
      result += art_char
    else:
      result += " "
  result += "\n"
print("NORMAL")
print(result)

inverted = ""
for i in range(ascii_max_x):
  for j in range(ascii_max_y):
    if img[(i, j)] > threshold:
      inverted += " "
    else:
      inverted += art_char
  inverted += "\n"
print("INVERTED")
print(inverted)
