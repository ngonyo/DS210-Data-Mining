import sys
import random
import re
import math
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import scipy

# This will tell me the dimensions of the image in pixels
photo = io.imread('cheetah-leaping.jpg')
print(photo.shape)
plt.imshow(photo)
plt.show()

# Show every other row of the photo
plt.imshow(photo[::2])
plt.show()

# Shrink the image by half
plt.imshow(photo[::2,::2])
plt.show()

# Show an upside down cheetah
plt.imshow(photo[::-1])
plt.show()

# Show only the cheetah head
plt.imshow(photo[60:125, :75])
plt.show()

# Show the cheetah whiteness
for x in range(324):
    for y in range(470):
        if (photo[x][y][0] >= 220 and photo[x][y][1] >= 220 and photo[x][y][2] >= 220):
            continue
        else:
            photo[x][y][0] = 0
            photo[x][y][1] = 0
            photo[x][y][2] = 0
plt.imshow(photo)
plt.show()