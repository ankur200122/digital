import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread("pust.png", cv2.IMREAD_GRAYSCALE)

# Step 1: Perform Fourier Transform
dft = np.fft.fft2(image)
dft_shifted = np.fft.fftshift(dft)  # Shift zero frequency component to the center

# Get image dimensions and center
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2  # Center of the image

# Step 2: Create Low-Pass and High-Pass Filter Masks
# Radius of the filter
radius = 30

# Low-Pass Filter Mask
low_pass_mask = np.zeros((rows, cols), np.uint8)
cv2.circle(low_pass_mask, (ccol, crow), radius, 1, thickness=-1)

# High-Pass Filter Mask (inverse of the low-pass)
high_pass_mask = 1 - low_pass_mask

# Step 3: Apply Filters in Frequency Domain
# Low-pass filter
low_pass_dft = dft_shifted * low_pass_mask
low_pass_ishifted = np.fft.ifftshift(low_pass_dft)
low_pass_image = np.fft.ifft2(low_pass_ishifted)
low_pass_image = np.abs(low_pass_image)

# High-pass filter
high_pass_dft = dft_shifted * high_pass_mask
high_pass_ishifted = np.fft.ifftshift(high_pass_dft)
high_pass_image = np.fft.ifft2(high_pass_ishifted)
high_pass_image = np.abs(high_pass_image)

# Step 4: Display the filtered images
plt.subplot(1, 2, 1)
plt.imshow(low_pass_image, cmap='gray')
plt.title("Low-Pass Filtered Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(high_pass_image, cmap='gray')
plt.title("High-Pass Filtered Image")
plt.axis('off')

plt.tight_layout()
plt.show()
