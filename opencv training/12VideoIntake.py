'''this thing is great, it takes in a camera video and outputs it in greyscale'''




import numpy as np
'''numpy is great, but it isnt used. I'd prefer to just always have it,
 and the compiler can decide if it wants to omit it'''

import cv2 as cv
"""opencv import, duh"""

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
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame

    '''same as above, but in real time. if camera cant read next frame, shoot out an error message'''

    """converts to greyscale"""

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break



# When everything done, release the capture
cap.release()
cv.destroyAllWindows()