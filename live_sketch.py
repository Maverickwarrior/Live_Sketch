import cv2
import numpy as np

def sketch(img):
    img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img_gaus = cv2.GaussianBlur(img_gray,(5,5),0)
    
    img_canny = cv2.Canny(img_gaus,5,30)
    
    ret,mask = cv2.threshold(img_canny,70,255,cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    
    cv2.imshow("Live Sketch",sketch(frame))
    
    if cv2.waitKey(1)==13:
        break
    
cap.release()
cv2.destroyAllWindows()    