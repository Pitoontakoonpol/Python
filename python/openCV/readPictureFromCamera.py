import cv2

cap = cv2.VideoCapture('VID_20200416_154531.mp4')
while (True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame: ',gray)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
    # if(cv2.waitKey(0)):
    #     break
    
cap.release()
cv2.destroyAllWindows()