import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread("pust.png", cv2.IMREAD_GRAYSCALE)

# Ask user for a 3x3 sharpening kernel input
print("Enter a 3x3 sharpening kernel row by row, with values separated by spaces.")
kernel_values = []
for i in range(3):
    row = input(f"Row {i+1}: ").strip().split()
    row = [float(val) for val in row]
    kernel_values.append(row)

# Convert the input into a 3x3 numpy array
sharpening_kernel = np.array(kernel_values)

# Apply the user-defined sharpening kernel to the image
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

# Display the original and sharpened images
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sharpened_image, cmap='gray')
plt.title("Sharpened Image")
plt.axis('off')

plt.tight_layout()
plt.show()
