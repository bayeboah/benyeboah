import cv2 as cv
import numpy


def click_event(event,x,y, flags, params):

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(cap,(x,y), 3, (0,0,255), -1)
        points.append((x,y))

        if len(points) >= 2:
            cv.line(cap, points[-1],points[-2], (0,0,255),1)

            cv.imshow('Live Feed',cap)
            print(points)




points =[]
cap = cv.VideoCapture(0)

while (cap.isOpened()==True):
    ret, frame = cap.read()

    if ret == True :

        cv.imshow('Live Feed', frame)
        cv.setMouseCallback('Live Feed', click_event)


        if cv.waitKey(1) & 0xFF == ord('q'): break


cap.release()
cv.destroyAllWindows()