import cv2
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread("pust.png", cv2.IMREAD_GRAYSCALE)

# Convert to binary using simple thresholding
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Display the binary image
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image")
plt.axis('off')
plt.show()
