import cv2
import numpy as np
import matplotlib.pyplot as plt
img =cv2.imread("pust.png")
height, width, _ = img.shape
# Create an empty array to store the grayscale image
gray_img = np.zeros((height, width),
dtype=np.uint8) 
# Convert the image to grayscale using a for loop
for i in range(height):
for j in range(width):
# Compute the mean of the BGR channels foreach pixel
gray_img[i][j] = np.mean(img[i][j])
# Create a binary image (black and white) based onthresholding
threshold = 127
bin_img = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
 for j in range(width):
if gray_img[i][j] > threshold: # Compareindividual pixel value
bin_img[i][j] = 255 # Set white pixel
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.subplot(1, 3, 2)
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image")
plt.subplot(1, 3, 3)
plt.imshow(bin_img, cmap='gray')
plt.title("Binary Image")
plt.show()   