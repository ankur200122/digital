import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert it to grayscale
image = cv2.imread("pust.png", cv2.IMREAD_GRAYSCALE)

# Apply Log Transformation
c_log = 255 / np.log(1 + np.max(image))  # Scaling constant
log_transformed = c_log * np.log(1 + image.astype(np.float64))  # Apply log transform
log_transformed = np.uint8(log_transformed)  # Convert back to uint8

# Apply Power-Law (Gamma) Transformation
gamma = 0.5  # Change gamma value for different effects
c_gamma = 255 / (np.max(image) ** gamma)  # Scaling constant
gamma_transformed = c_gamma * (image.astype(np.float64) ** gamma)  # Apply power-law transform
gamma_transformed = np.uint8(gamma_transformed)  # Convert back to uint8

# Display the images
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(log_transformed, cmap='gray')
plt.title("Log Transformed")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(gamma_transformed, cmap='gray')
plt.title("Gamma Transformed")
plt.axis('off')

plt.tight_layout()
plt.show()
