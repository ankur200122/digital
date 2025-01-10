import cv2
import matplotlib.pyplot as plt

image = cv2.imread('pust.png',cv2.IMREAD_GRAYSCALE)

gaussian_blur = cv2.GaussianBlur(image, (9, 9), 0)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(gaussian_blur, cmap='gray')
axes[1].set_title('Blurred Image')
axes[1].axis('off')

plt.show()