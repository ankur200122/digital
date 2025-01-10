import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread("pust.png")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for matplotlib

# Prompt user for padding size
top = int(input("Enter the padding size for the top: "))
bottom = int(input("Enter the padding size for the bottom: "))
left = int(input("Enter the padding size for the left: "))
right = int(input("Enter the padding size for the right: "))

# Prompt user for padding color (as RGB values)
print("Enter the padding color (R, G, B) values:")
r = int(input("R: "))
g = int(input("G: "))
b = int(input("B: "))

# Add padding to the image
padded_image = cv2.copyMakeBorder(
    image_rgb, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[r, g, b]
)

# Display original and padded images
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(padded_image)
plt.title("Padded Image")
plt.axis('off')

plt.tight_layout()
plt.show()
