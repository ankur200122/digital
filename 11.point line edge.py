import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread("pust.png", cv2.IMREAD_GRAYSCALE)

# Function to get a custom kernel from user input
def get_custom_kernel():
    print("Enter a 3x3 kernel row by row, with values separated by spaces.")
    kernel_values = []
    for i in range(3):
        row = input(f"Row {i+1}: ").strip().split()
        row = [float(val) for val in row]
        kernel_values.append(row)
    return np.array(kernel_values)

# Get user-defined kernels for point, line, and edge detection
print("Define a kernel for point detection:")
point_kernel = get_custom_kernel()

print("Define a kernel for line detection:")
line_kernel = get_custom_kernel()

print("Define a kernel for edge detection:")
edge_kernel = get_custom_kernel()

# Apply the custom kernels
point_detected = cv2.filter2D(image, -1, point_kernel)
line_detected = cv2.filter2D(image, -1, line_kernel)
edge_detected = cv2.filter2D(image, -1, edge_kernel)

# Display results
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(point_detected, cmap='gray')
plt.title("Point Detection (Custom Kernel)")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(line_detected, cmap='gray')
plt.title("Line Detection (Custom Kernel)")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(edge_detected, cmap='gray')
plt.title("Edge Detection (Custom Kernel)")
plt.axis('off')

plt.tight_layout()
plt.show()
