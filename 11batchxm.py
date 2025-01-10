import cv2
import numpy as np
import matplotlib.pyplot as plt

# Specify the image path and padding size
image_path = 'pust.png'  # Replace with your image path
padding_size = 20  # Size of the padding

# Read the input image in grayscale
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError(f"The image at {image_path} could not be found.")

# Calculate the boundary pixel values using explicit for loops
boundary_values = []
for i in range(image.shape[1]):
    boundary_values.append(image[0, i])  # Top boundary
    boundary_values.append(image[-1, i])  # Bottom boundary
for i in range(image.shape[0]):
    boundary_values.append(image[i, 0])  # Left boundary
    boundary_values.append(image[i, -1])  # Right boundary

# Calculate the mean using a for loop
total_sum = 0
count = 0
for value in boundary_values:
    total_sum += value
    count += 1

boundary_average = total_sum // count  # Use integer division for the average

# Add padding using the average of the boundary values
rows, cols = image.shape
padding_rows = rows + 2 * padding_size
padding_cols = cols + 2 * padding_size
image_with_padding = np.zeros((padding_rows, padding_cols), dtype=image.dtype)

# Fill the central part with the original image
image_with_padding[padding_size:-padding_size, padding_size:-padding_size] = image

# Fill the padding with the average boundary value
for i in range(padding_size):
    # Top and bottom padding
    image_with_padding[i, :] = boundary_average
    image_with_padding[-(i + 1), :] = boundary_average

    # Left and right padding
    image_with_padding[:, i] = boundary_average
    image_with_padding[:, -(i + 1)] = boundary_average

# Display the original and output images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Image with Padding")
plt.imshow(image_with_padding, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.show()