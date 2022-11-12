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

'''Because we want our window to be displayed until the user presses a key 
(otherwise the program would end far too quickly), we use the cv::waitKey function 
whose only parameter is just how long should it wait for a user input (measured in milliseconds). 
Zero means to wait forever. The return value is the key that was pressed.'''

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)


    '''In the end, the image is written to a file if the pressed key was the "s"-key.
     For this the cv::imwrite function is called that has the file path and the cv::Mat
      object as an argument.'''

