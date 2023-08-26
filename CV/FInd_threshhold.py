import cv2, numpy


def nothing(x):
    print(x)

img = cv2.imread('trial_data/squirrel_cls.jpg')
imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Image')

#

cv2.createTrackbar('th','Image', 0, 255, nothing)


while(1):

    th = cv2.getTrackbarPos('th', 'Image')

    _, thresh = cv2.threshold(imgrey, th, 255, cv2.THRESH_BINARY)

    cv2.imshow('Image', thresh)

    k = cv2.waitKey(1) & 0xff
    if k == 27 :
        break


cv2.destroyWindow()