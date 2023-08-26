import cv2
import numpy as np


def change(x):
    print(x)

#img = cv2.imread('trial_data/butterfly.jpg')
img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow('Image')
cv2.createTrackbar('B','Image',0,255, change)
cv2.createTrackbar('G','Image',0,255, change)
cv2.createTrackbar('R','Image',0,255, change)

switch = '0 : Off \n 1: On'
cv2.createTrackbar(switch, 'Image', 0,1, change)


while(1):

    cv2.imshow('Image',img)

    k= cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

    b = cv2.getTrackbarPos('B','Image')
    g = cv2.getTrackbarPos('G', 'Image')
    r = cv2.getTrackbarPos('R', 'Image')
    s = cv2.getTrackbarPos(switch, 'Image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]





cv2.destroyAllWindows()