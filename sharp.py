import cv2
import matplotlib.pyplot as plt

image = cv2.imread('pust.png',cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(image, (9, 9), 10.0)

sharpened = cv2.addWeighted(image, 1.5, blurred, 0.2, 0)
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(sharpened, cmap='gray')
axes[1].set_title('Sharpened Image')
axes[1].axis('off')

plt.show()
