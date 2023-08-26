import copy
import cv2


def click_event(event,x,y, flags, params):

        #Mouse event
        if event == cv2.EVENT_LBUTTONDOWN:
                cv2.circle(img, (x,y),3,(0,255,255),-1)
                points.append((x,y))

                if len(points) >= 2 :
                        cv2.line(img ,points[-1] , points[-2] , 1)

                cv2.imshow('image',img)

                print(points)


img = cv2.imread('trial_data/rubberwhale1.png')
points =[]


cv2.namedWindow('image')


cv2.setMouseCallback('image',click_event)

while(1):
        cv2.imshow('image', img)
        k= cv2.waitKey(0) & 0xff
        if k == 27 :
                break
       

cv2.destroyAllWindows()




