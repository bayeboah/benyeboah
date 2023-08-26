import cv2
import  matplotlib.pyplot as plt

img = cv2.imread('trial_data/squirrel_cls.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,th= cv2.threshold(img, 200, 255 , cv2.THRESH_BINARY)
th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,179,5)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 179, 5)

images = [img, th,th1,th2]
titles =['Original_Image', 'Simple_thres','Adaptive_thres1','Adaptive_thres2']

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.yticks([]),plt.xticks([])

plt.show()




k = cv2.waitKey(0) & 0xff
if k == ord('q') :
    cv2.destroyAllWindows()