'''this will be my first custom program,
I will be pulling from previous learning for this code

this is a simple orb-finding video program,
it take real-time video and overlays significant markers'''


import numpy as np
'''numpy is great, but it isnt used. I'd prefer to just always have it,
 and the compiler can decide if it wants to omit it'''

import cv2 as cv
"""opencv import, duh"""

from __future__ import print_function
import argparse


from matplotlib import pyplot as plt
'''pyplot, for orb stuff i think'''



cap = cv.VideoCapture(0)
'''set a name to the video input'''
if not cap.isOpened():
    print("Cannot open camera")
    exit()
'''shoots out an error message if video cant open, great error-checking shenanigans'''


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True

    # Initiate ORB detector
    orb = cv.ORB_create()
    # find the keypoints with ORB
    kp = orb.detect(frame, None)


    # compute the descriptors with ORB
    kp, des = orb.compute(frame, kp)

    # draw only keypoints location,not size and orientation
    frame2 = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)

    #plt.imshow(frame2), plt.show()
    """this would usually be used to output the orbs calculated above, but we are passing to the live feed"""

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    # Display the resulting frame

    '''same as above, but in real time. if camera cant read next frame, shoot out an error message'''
    """converts to greyscale"""

    cv.imshow('frame', frame2)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()


