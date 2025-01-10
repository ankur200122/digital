import cv2
import matplotlib.pyplot as plt
#image =cv2.imread("./1.jpeg")

#image = cv2.imread("./pust.png")
#image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.imread('pust.png', cv2.IMREAD_GRAYSCALE)

plt.imshow(image,cmap='gray')
plt.show()