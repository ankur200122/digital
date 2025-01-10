import cv2
import numpy as np
import matplotlib.pyplot as plt

#image input

image = cv2.imread('pust.png', cv2.IMREAD_GRAYSCALE)

#histogram of original image

row,col = image.shape

y = np.zeros((256),np.uint64)

for i in range(row):
    for j in range(col):
       y[image[i,j]]+=1

x = np.arange(0,256)

#histogram equalization

levels = 256
histogram = [0]*levels
for i in range(row):
    for j in range(col):
        pixel_value = image[i,j]
        histogram[pixel_value]+=1

cumsum = [0]*levels
cumsum[0] = histogram[0]

for i in range(1,levels):
    cumsum[i] = cumsum[i-1] + histogram[i]

total_pixels = row*col

normal_cus = [int(c*(levels-1)/total_pixels) for c in cumsum]

equalized_image = np.zeros_like(image)

for i in range(row):
    for j in range(col):
        original_v = image[i,j]
        equalized_image[i,j] = normal_cus[original_v]


#histogram of equalized image

row,col = equalized_image.shape

y1 = np.zeros((256),np.uint64)

for i in range(row):
    for j in range(col):
       y1[equalized_image[i,j]]+=1

x1 = np.arange(0,256)


#apply filter

kernel = np.array([[-1,-1,-1],
                   [0,8,0],
                   [-1,-1,-1]])

filter_image = cv2.filter2D(image, -1,  kernel)

#histogram of equalized image

row,col = equalized_image.shape

y2 = np.zeros((256),np.uint64)

for i in range(row):
    for j in range(col):
       y2[filter_image[i,j]]+=1

x2 = np.arange(0,256)

#show images




# Display the images
plt.subplot(2, 3, 1)
plt.imshow(image , cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.bar(x, y, color='red' , align='center')
plt.title("Histogram of original image")


plt.subplot(2, 3, 2)
plt.imshow(equalized_image , cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.bar(x1, y1, color='red' , align='center')
plt.title("Histogram of equalized image")


plt.subplot(2, 3, 3)
plt.imshow(filter_image , cmap='gray')
plt.title('Filter image')
plt.axis('off')

plt.subplot(2,3,6)
plt.bar(x2,y2,color='red',align='center')

plt.title('Histogram of filter image')


plt.tight_layout()
plt.show()
