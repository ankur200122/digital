import numpy as np
#from PIL import Image
import cv2

# Load the image and convert it to grayscale
#image = Image.open('pust.png').convert('L')

image=cv2.imread('pust.png',cv2.IMREAD_GRAYSCALE)
image_array = np.array(image)
# Get the dimensions of the image
rows, cols = image_array.shape

# Extract the boundary elements
top_row = image_array[0, :]
bottom_row = image_array[-1, :]
left_column = image_array[:, 0]
right_column = image_array[:, -1]

# Concatenate all boundary elements
boundary_elements = np.concatenate((top_row, bottom_row, left_column[1:-1], right_column[1:-1]))

# Sum of boundary elements
boundary_sum = np.sum(boundary_elements)

print("Boundary Elements:", boundary_elements)
print("Sum of Boundary Elements:", boundary_sum)
