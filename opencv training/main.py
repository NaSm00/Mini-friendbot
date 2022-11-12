import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("starry_night.jpg"))

'''IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.
IMREAD_UNCHANGED loads the image as is (including the alpha channel if present)
IMREAD_GRAYSCALE loads the image as an intensity one'''

if img is None:
    sys.exit("Could not read the image.")

'''Afterwards, a check is executed, if the image was loaded correctly.'''



cv.imshow("Display window", img)



k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)

