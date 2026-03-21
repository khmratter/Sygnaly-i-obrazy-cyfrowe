import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('beachside.jpg')            # It is needed to be in this folder to be able to upload the image
image = cv.cvtColor(img, cv.COLOR_BGR2RGB)

def appr_dim(obraz):
  height, width = image.shape[:2]
  if height % 2 != 0 : height -= 1
  if width % 2 != 0 : width -= 1
  obraz = obraz[:height, :width]
  return obraz

image = appr_dim(image)
plt.imshow(image)
plt.show()


def rotating(obraz, angle):
  height, width = obraz.shape[:2]

  center = (width/2, height/2)
  rotate_matrix = cv.getRotationMatrix2D(center, angle, 1)
  rotated_image = cv.warpAffine(obraz, rotate_matrix, dsize=(width, height))

  return rotated_image


kat = range(0, 361, 12)
for i in kat:
  plt.imshow(rotating(image, i))      # Creating a series of images of rotated original image by 360 degrees with a step of 12 degrees
  plt.show()


last_image = rotating(image, kat[-1])
plt.imshow(image - last_image)        # No differences between input and output images 
plt.show()



obrocony = rotating(image, 45)      # Rotated image by 45 degrees
plt.imshow(obrocony)
plt.show()
z_powrotem = rotating(image, 135)    # Rotating the original image by 135 degrees
plt.imshow(z_powrotem)
plt.show()


def downsizing(image):
  height, width = image.shape[:2]
  small_height, small_width = int(height*0.5), int(width*0.5)
  downsized_image = np.zeros((small_height, small_width, 3), dtype=np.uint8)

  for row in range(0, small_height):
    for column in range(0, small_width):
      downsized_image[row][column] = image[row*2][column*2]

  return downsized_image


zmniejszony = downsizing(image)
plt.subplot(1,2,1)
plt.imshow(zmniejszony)
plt.subplot(1,2,2)        # Comparing two images, the original one and the downsized one, side by side but with different scales
plt.imshow(image)


def upsizing(image):
  height, width = image.shape[:2]
  big_height, big_width = height*2, width*2
  upsized_image = np.zeros((big_height, big_width, 3), dtype=np.uint8)

  for row in range(height):
    for column in range(width):
      upsized_image[row*2][column*2] = image[row][column]

  return upsized_image


zwiekszony = upsizing(zmniejszony)      # Upsizing the downsized earlier image to get the original one 
plt.subplot(1,2,1)        # The picture is darker than the original one because of the missing values
plt.imshow(zwiekszony)    # There is not enough information to restore the original image just by upsizing 
plt.subplot(1,2,2)        # We have to use interpolation function to fill in those values
plt.imshow(image)
plt.show()
plt.imshow(zwiekszony)


def interpolation(obrazek):

  kernel = np.ones((2,2), np.float32)
  obrazek = cv.filter2D(obrazek, -1, kernel)

  return obrazek


interpolowany = interpolation(zwiekszony)     # Interpolated upsized image
plt.imshow(interpolowany)       # The image isn't dark anymore, we've estimatated the missing colour values using interpolation
plt.show()

plt.imshow(image - interpolowany)     # The differences between the original image and the scaled and interpolated one 
plt.show()                            # As we can see the information is mostly lost on the edges of objects