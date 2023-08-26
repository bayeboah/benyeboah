import cv2
import matplotlib

img = cv2.imread('trial_data/M17_01.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurr = cv2.GaussianBlur(gray,(5,5),0)
_, thresh = cv2.threshold(blurr,114,255,cv2.THRESH_BINARY)
dil = cv2.dilate(thresh, None, iterations=3)

contours,_ =cv2.findContours(dil,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,1,(0,255,0),2)

cv2.imshow('Boil',img)
k = cv2.waitKey(0) & 0xff
if k == 27:
    cv2.destroyAllWindows()