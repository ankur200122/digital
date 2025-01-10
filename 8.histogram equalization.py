import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread("pust.png", cv2.IMREAD_GRAYSCALE)

# Step 1: Calculate the histogram
histogram = np.zeros(256, dtype=int)
for pixel_value in image.flatten():
    histogram[pixel_value] += 1

# Step 2: Compute the CDF
cdf = histogram.cumsum()  # Cumulative sum to get the cumulative distribution function
cdf_normalized = cdf * (255 / cdf[-1])  # Normalize to range 0-255

# Step 3: Use CDF to map original pixel values to equalized values
equalized_image = np.zeros_like(image)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        equalized_image[i, j] = cdf_normalized[image[i, j]]
        
        row,col = equalized_image.shape

y1 = np.zeros((256),np.uint64)

for i in range(row):
    for j in range(col):
       y1[equalized_image[i,j]]+=1

x1 = np.arange(0,256)

# Step 4: Display the original and equalized images
plt.subplot(3, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(3, 3, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title("Equalized Image")
plt.axis('off')

plt.subplot(3, 3, 3)
plt.bar(x1, y1, color='red' , align='center')
plt.title("Histogram of equalized image")
plt.tight_layout()
plt.show()
