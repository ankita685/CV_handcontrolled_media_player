import cv2
import numpy as np
def nothing(x):
    pass
def createTrackbar():
    cv2.namedWindow("thresholding")
    #cv2.createTrackbar("T","thresholding",0,255,nothing)
    cv2.getTrackbarPos("H_min","thresholding")
    cv2.getTrackbarPos("H_max","thresholding")
    cv2.getTrackbarPos("S_min","thresholding")
    cv2.getTrackbarPos("S_max","thresholding")
    cv2.getTrackbarPos("V_min","thresholding")
    cv2.getTrackbarPos("V_max","thresholding")

img = cv2.imread("C:/Users/pc/OneDrive/Desktop/workshop/emr_day_2/images/hand.jpg")
cv2.imshow("original image",img)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray scale image",gray_scale)



createTrackbar()

while True:
   # T = cv2.getTrackbarPos("T","thresholding")
    H_min = cv2.getTrackbarPos("H_min","thresholding")
    H_max = cv2.getTrackbarPos("H_max","thresholding")
    S_min = cv2.getTrackbarPos("S_min","thresholding")
    S_max = cv2.getTrackbarPos("S_max","thresholding")
    V_min = cv2.getTrackbarPos("V_min","thresholding")
    V_max = cv2.getTrackbarPos("V_max","thresholding")

    #print(T)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #lower =np.array([0,0,0])
    #upper = np.array([100,255,255])
    lower =np.array([H_min,S_min,V_min])
    upper = np.array([H_max,S_max,V_max])
    thresh_img =cv2.inRange(img_hsv,lower,upper)
    cv2.imshow("thresh_img",thresh_img)

   # _,thresh_img =cv2.threshold(gray_scale,T,255,cv2.THRESH_BINARY)
    #cv2.imshow("thresh_img",thresh_img)
    
    key = cv2.waitKey(1)
    if(key==ord('q')):
        break
 
cv2.waitKey(0)
cv2.destroyAllWindows()
