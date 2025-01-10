import cv2
import numpy as np
import matplotlib.pyplot as plt

#image input

image = cv2.imread('abc.jpeg', cv2.IMREAD_GRAYSCALE)

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

fig,axes = plt.subplots(2,3,figsize=(14,5))

axes[0,0].imshow(image , cmap='gray')
axes[0,0].set_title('Original Image')
axes[0,0].axis('off')

axes[1,0].bar(x, y, color='red' , align='center')
axes[1,0].set_title('Histogram of Original Image')

axes[0,1].imshow(equalized_image , cmap='gray')
axes[0,1].set_title('Equalized Image')
axes[0,1].axis('off')

axes[1,1].bar(x1, y1, color='red' , align='center')
axes[1,1].set_title('Histogram of Equalized Image')

axes[0,2].imshow(filter_image , cmap='gray')
axes[0,2].set_title('Filter Image')
axes[0,2].axis('off')

axes[1,2].bar(x2, y2, color='red' , align='center')
axes[1,2].set_title('Histogram of Filtered Image')

plt.show()