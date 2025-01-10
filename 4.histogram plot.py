import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Read the image and convert to grayscale
image = cv2.imread('pust.png', cv2.IMREAD_GRAYSCALE)

# Step 2: Get the dimensions of the image
rows, cols = image.shape
total_pixels = rows * cols  # Total number of pixels in the image

# Step 3: Initialize an array to store the frequency of each pixel intensity (0-255)
histogram = np.zeros((256),np.uint64)

# Step 4: Calculate the frequency of each pixel intensity
for i in range(rows):
    for j in range(cols):
        pixel_value = image[i, j]  # Get the pixel intensity
        histogram[pixel_value] += 1  # Increment the count for that intensity

# Step 5: Convert frequencies to probabilities
# Divide each intensity count by the total number of pixels to get the probability
probabilities = histogram / total_pixels

# Step 6: Plot the probabilities as a histogram
x = np.arange(256)  # The range of pixel intensities (0 to 255)
plt.bar(x, probabilities, color='gray', align='center')
plt.xlabel('Pixel Intensity')
plt.ylabel('Probability')
plt.title('Grayscale Histogram (Probability Distribution)')
plt.show()
