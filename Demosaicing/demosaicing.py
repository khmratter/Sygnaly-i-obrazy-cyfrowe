import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Passiflora_caerulea.jpg')      # It is needed to be in this folder to be able to upload the image

plt.axis('off')
plt.imshow(img)
plt.show()


#BayerMask = np.array([[[0, 1], [0, 0]],
#                         [[1, 0], [0, 1]],
#                         [[0, 0], [1, 0]]], np.uint8)  - visualising as matrix Bayer mask

def bayer(image):           # Simulating image sensor with Bayer filter
  length = len(image)
  width = len(image[0])
  bayer = np.zeros_like(image)
  for row in range (length):
    for column in range (width):
      if (row%2 == 1 and column%2 == 1):
        bayer[row, column] = [image[row, column, 0], 0, 0]      #blue
      elif (row%2 == 0 and column%2 == 0):
        bayer[row, column] = [0, 0, image[row, column, 2]]      #red
      else:
        bayer[row, column] = [0, image[row, column, 1], 0]     #green

  return bayer


def x_trans(image):         # Simulating image sensor with Fuji X-Trans filter
  length = len(image)
  width = len(image[0])
  x_trans = np.zeros((length, width, 3), np.uint8)
  for row in range (0, length):
    for column in range (0, width):
      if (row%6 == 0 and column%6 == 1) or (row%6 == 0 and column%6 == 5) or (row%6 == 1 and column%6 == 3) or (row%6 == 2 and column%6 == 0) or (row%6 == 3 and column%6 == 2) or (row%6 == 3 and column%6 == 4) or (row%6 == 4 and column%6 == 0) or (row%6 == 5 and column%6 == 3): #blue
      
        x_trans[row][column] = [image[row][column][0], 0, 0]
      elif (row%6 == 0 and column%6 == 2) or (row%6 == 0 and column%6 == 4) or (row%6 == 1 and column%6 == 0) or (row%6 == 2 and column%6 == 3) or (row%6 == 3 and column%6 == 1) or (row%6 == 3 and column%6 == 5) or (row%6 == 4 and column%6 == 3) or (row%6 == 5 and column%6 == 0): #red
      
        x_trans[row][column] = [0, 0, image[row][column][2]]
      else:
      #((row%6 == 0 or row%6 == 3) and (column%6 == 0 or column%6 == 3)) or ((row%6 == 1 or row%6 == 2 or row%6 == 4 or row%6 == 5) and (column%6 == 1 or column%6 == 2 or column%6 == 4 or column%6 == 5)): #green
        x_trans[row][column] = [0, image[row][column][1], 0]

  return x_trans

plt.imshow(bayer(img))    # Mosaicing image using Bayer filter
plt.axis('off')
plt.show()

plt.imshow(x_trans(img))    # Mosaicing image using Fuji X-Trans filter
plt.axis('off')
plt.show()


def bayer_demosaic(image):          # Reconstructing (demosaicing) of a Bayer format image (Bayer interpolation)

  length = len(image)
  width = len(image[0])
  demosaic = np.zeros((length, width, 3), np.uint8)

  B, G, R = cv.split(image)
  kernelGreen = np.ones((2,2), np.float32)/2
  kernelRedBlue = np.ones((2,2), np.float32)

  demosaic[:,:,2] = cv.filter2D(R, -1, kernelRedBlue)    #red
  demosaic[:,:,0] = cv.filter2D(B, -1, kernelRedBlue)    #blue
  demosaic[:,:,1] = cv.filter2D(G, -1, kernelGreen)      #green

  return demosaic

def x_trans_demosaic(image):        # Reconstructing (demosaicing) of a X-Trans format image (Fuji X-Trans interpolation)

  length = len(image)
  width = len(image[0])
  demosaic = np.zeros((length, width, 3), np.uint8)

  B, G, R = cv.split(image)
  kernelGreen = np.ones((3,3), np.float32)/5
  kernelRedBlue = np.ones((3,6), np.float32)/4

  demosaic[:,:,2] = cv.filter2D(R, -1, kernelRedBlue) #red
  demosaic[:,:,0] = cv.filter2D(B, -1, kernelRedBlue) #blue
  demosaic[:,:,1] = cv.filter2D(G, -1, kernelGreen) #green

  return demosaic


demosaic_bayer = bayer_demosaic(bayer(img))     # Demosaiced Bayer image 
plt.imshow(demosaic_bayer)
plt.axis('off')
plt.show()

demosaic_x_trans = x_trans_demosaic(x_trans(img))    # Demosaiced X-Trans image
plt.imshow(demosaic_x_trans)
plt.axis('off')
plt.show()

plt.imshow(img - demosaic_bayer)        # Differences between original image and demosaiced one (Bayer) 
plt.axis('off')
plt.show()

plt.imshow(img - demosaic_x_trans)      # Differences between original image and demosaiced one (Fuji X-Trans) 
plt.axis('off')
plt.show()

# The images mostly differ at edges - loss of information, less visible colour or roughness 