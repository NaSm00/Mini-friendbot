import cv2 as cv
import numpy as np



'''this code is a small subset of image filters for intake,
they help remove unwanted noise and other artifacts. here is the hyperlink to other options 
beside the one demonstrated below

https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html'''


img = cv.imread('j.png',0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
cv.imshow("Display window", erosion)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("j.png", img)



