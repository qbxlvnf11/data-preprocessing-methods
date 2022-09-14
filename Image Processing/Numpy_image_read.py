import PIL.Image as pilimg
import numpy as np

path = './example.jpg'

# Read image
img = pilimg.open(path)

# Display image
img.show()

# Fetch image pixel data to numpy array
pix = np.array(img)
