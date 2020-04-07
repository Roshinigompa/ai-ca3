import numpy as np
import cv2


cap=cv2.VideoCapture(0)
while(True):
    ret,fram=cap.read()
    frame=fram
    g=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    img_item = 'my-image.png'
    cv2.imwrite(img_item,frame)    

    cv2.imshow('CAMERA',fram)
    

    
    if cv2.waitKey(1) & 0xFF==ord('q'):        
        break
    
cap.release()
cv2.destroyAllWindows()
