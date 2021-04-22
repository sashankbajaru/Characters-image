import cv2
import numpy as np

# method to find the corresponding character for an intensity level
# The idea is if the intesity level is high, the character occupies less number of pixels on screen
def find_char(ints):  # ints is the intensity level of the block
  if(ints<255/9):
    return "#"
  elif(ints<(256*2)/9):
    return "@"
  elif(ints<(256*3)/9):
    return "%"
  elif(ints<(256*4)/9):
    return "="
  elif(ints<(256*5)/9):
    return "+" 
  elif(ints<(256*6)/9):
    return "*"
  elif(ints<(256*7)/9):
    return ":"
  elif(ints<(256*8)/9):
    return "-"
  else:
    return "."

image_file = 'your_image.jpg' # your image file name here.

img = cv2.imread(image_file, 0)
img_x = 300  # adjust these according to the output size
img_y = int(350*(img.shape[1]/img.shape[0]))
img = cv2.resize(img,(img_x, img_y)) 

# In the below loop we are dividing the image into blocks of size 6x3 pixels each
for i in range(0,int(img.shape[0]/6)):
  line = ""
  for j in range(0,int(img.shape[1]/3)):
    ints = 0     # sum of intensities
    for k in range(0,6):
      for m in range(0,3):
        ints = ints+(img[6*i+k][3*j+m])
    ints = ints/18   # average of intensities
    line+=find_char(ints)  # find the respective character for the intensity
  print(line)
