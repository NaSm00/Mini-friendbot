'''


here is a link to the page, as it has helpful thoughts and links for optimization and efficiency

https://docs.opencv.org/4.x/dc/d71/tutorial_py_optimization.html


additionally,this is just a repository of things, not a running code.

'''


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


'''The cv.getTickFrequency function returns the frequency of clock-cycles,
 or the number of clock-cycles per second. So to find the time of execution in seconds,
  you can do following:'''
e1 = cv.getTickCount()
# your code execution
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()


'''We will demonstrate with following example. The following example applies median filtering 
with kernels of odd sizes ranging from 5 to 49. (Don't worry about what the result will look like 
- that is not our goal):'''

img1 = cv.imread('messi5.jpg')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
# Result I got is 0.521107655 seconds





''''''
