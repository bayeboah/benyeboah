import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('trial_data/Car.jpg',1)

lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)

sobel_Combined = cv2.bitwise_or(sobelx,sobely)

titles = ['laplacian','sobelx','sobely','sobel_combined']
images = [lap,sobelx,sobelx,sobel_Combined]

for i in range(4):
    plt.subplot(2,2, i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()

