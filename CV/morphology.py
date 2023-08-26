import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('trial_data/WhiteHat.png',0)

_, mask = cv.threshold(img,230,255, cv.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
elip = cv.getStructuringElement(cv.MORPH_RECT,(5,5))

#var = cv.morphologyEx(mask,cv.MORPH_ELLIPSE,elip)
var = cv.filter2D(img,0,elip)


titles = ['original','mask','var']
images = [img, mask,var] 

for i in range(3):
    plt. subplot(2,2, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
