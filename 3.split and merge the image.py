import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("pust.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for display

# Get the image dimensions
height, width, _ = image.shape

# Split the image into 4 quadrants
top_left = image_rgb[0:height//2, 0:width//2]
top_right = image_rgb[0:height//2, width//2:width]
bottom_left = image_rgb[height//2:height, 0:width//2]
bottom_right = image_rgb[height//2:height, width//2:width]

# Merge the quadrants back into one image
top = np.hstack((top_left, top_right))      # Stack top-left and top-right horizontally
bottom = np.hstack((bottom_left, bottom_right))  # Stack bottom-left and bottom-right horizontally
merged_image = np.vstack((top, bottom))          # Stack top and bottom vertically to get the complete image

# Display the images
plt.subplot(2, 3, 1)
plt.imshow(top_left)
#plt.imshow(image,cmap='gray')
plt.title("Top Left")
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(top_right)
plt.title("Top Right")
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(bottom_left)
plt.title("Bottom Left")
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(bottom_right)
plt.title("Bottom Right")
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(merged_image)
plt.title("Merged Image")
plt.axis('off')

plt.tight_layout()
plt.show()
