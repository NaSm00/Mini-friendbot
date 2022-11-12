import numpy as np



#having some issues here as well


import cv2 as cv
im = cv.imread('test.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

while True:

    cv.imshow('frame', imgray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()