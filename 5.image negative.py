import cv2
import numpy as np


image = cv2.imread('pust.png', cv2.IMREAD_GRAYSCALE)


negative_image = 255 - image

cv2.imshow('Negative Image', negative_image)
#cv2.imwrite('negative_image.png', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
