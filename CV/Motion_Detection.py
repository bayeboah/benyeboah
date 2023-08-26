import cv2
import numpy as np

#cap = cv2.VideoCapture('data/vtest.avi')
cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()


while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2) # finding the absolute difference between the frame.
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # it easy to find the contours in gray scale mode more than the colored mode
    blurr = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blurr, 20, 255, cv2.THRESH_BINARY) #Separating objects from background
    dilated = cv2.dilate(thresh, None, iterations= 3) #dialate the thresholding image to  file the holes which helps with dilation
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # iteration over the contours to retrieve the rectangle
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900 :
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, 'Status: {}'.format('movement'),(10,20), cv2.FONT_HERSHEY_SIMPLEX, 1 , (0, 0, 255), 3)


    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)



    cv2.imshow('Feed', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break


cv2.destroyWindow()
cap.release()