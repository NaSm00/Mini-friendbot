import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



img = cv.imread('opencv_logo.png')

'''below is the simplified Convolutional 5*5 matrix, the dst image uses the filter2d command
to convolve the matrix and take the average, blurring the image slightly

https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html

there are a few more filtering options, So I am adding the hyperlink'''
kernel = np.ones((5,5),np.float32)/25

dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')

plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(dst),plt.title('Averaging')

plt.xticks([]), plt.yticks([])
plt.show()