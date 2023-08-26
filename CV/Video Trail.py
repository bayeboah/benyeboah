import cv2
import datetime


cap = cv2.VideoCapture(0)

while(cap.isOpened()==True):
    ret, frame = cap.read()

    if ret == True :
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


        font = cv2.FONT_HERSHEY_SIMPLEX
        text= str(datetime.datetime.now())
        frames = cv2.putText(frame,text,(10,50),font,1 ,(0,255,0),2, cv2.LINE_AA)

        cv2.imshow('Video', frames)


        if cv2.waitKey(1) & 0xff == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()