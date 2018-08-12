import cv2
import numpy as np

videocapture=cv2.VideoCapture('F:\\Dead Poets Society.RMVB')
while(1):
        ret,frame=videocapture.read()
        cv2.imshow("capture", frame)
        cv2.waitKey (30)

cv2.destroyAllWindows()