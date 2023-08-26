import cv2 ,copy


image = cv2.imread('trial_data/rubberwhale1.png')
clone = image.copy()
refPt = []
count = 0

# left click to draw the next line, right click to delete the previous line
def draw_line(event, x, y, flags, param):
    global refPt, count, image
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x, y))
        cv2.line(image, refPt[count-1], refPt[count], (0, 255, 0), 1)
        count = count + 1


    elif event == cv2.EVENT_RBUTTONDOWN:
        image = clone.copy()
        refPt.remove(refPt[count-1])
        count = count - 1
        for i in range (1, count):
            cv2.line(image, refPt[i-1], refPt[i], (0,255,0), 1)

cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_line)

while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    # if the 'reset' key is pressed, reset to original state
    if key == ord("r"):
        image = clone.copy()
    # if the 'exit' key is pressed, break from the loop
    elif key == ord("e"):
        break

cv2.destroyAllWindows()