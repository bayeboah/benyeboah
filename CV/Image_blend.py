import cv2
import numpy as np


img = cv2.imread('trial_data/ben_2.png')
img_2 = cv2.imread('trial_data/lena.jpg')

#resizing image
img = cv2.resize(img, (512, 512))
img_2 = cv2.resize(img_2, (512, 512))

#size
print(img_2.shape)
print(img.shape)



#Gaussian pyramid for ben
ben_copy = img.copy()
gp_ben = [ben_copy]

for i in range(6):
    ben_copy = cv2.pyrDown(ben_copy)
    gp_ben.append(ben_copy)


#Gaussian pyramid for lena
lena_copy = img_2.copy()
gp_lena = [lena_copy]

for i in range(6):
    lena_copy = cv2.pyrDown(lena_copy)
    gp_lena.append(lena_copy)




#laplacian Pyramid for Ben
ben_copy = gp_ben[5]
lp_ben = [ben_copy]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_ben[i])
    laplacian = cv2.subtract(gp_ben[i-1], gaussian_extended)
    lp_ben.append(laplacian)

#laplacian Pyramid for Lena
lena_copy = gp_lena[5]
lp_lena = [lena_copy]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_lena[i])
    laplacian = cv2.subtract(gp_lena[i-1], gaussian_extended)
    lp_lena.append(laplacian)


#Adding  of the Images
ben_lena_pyramid = []
n = 0
for ben_lap, lena_lap in zip(lp_ben, lp_lena):
    n += 1
    cols, rows, ch = lena_lap.shape
    laplacian = np.hstack((ben_lap[:, :int(cols/2)], lena_lap[:, int(cols/2):]))
    ben_lena_pyramid.append(laplacian)

#Image recontruction
ben_Lena_reconstruct= ben_lena_pyramid[0]

for i in range(1, 6):
    ben_Lena_reconstruct = cv2.pyrUp(ben_Lena_reconstruct)
    ben_Lena_reconstruct = cv2.add(ben_lena_pyramid[i], ben_Lena_reconstruct)








cv2.imshow('Ben', img)
cv2.imshow('Lena', img_2)
cv2.imshow('Blending', ben_Lena_reconstruct)

k= cv2.waitKey(0) & 0xff
if k == 27:
    cv2.destroyWindows()
