import cv2
#import numpy as np

img_path = "./emr_day_2/images/gray_scale.png"
img  = cv2.imread(img_path)
gray_scale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ("img",img)
#cv2.imshow("IMG",img)



_,thresh_img = cv2.threshold(gray_scale_img,50,255,cv2.THRESH_BINARY)
cv2.imshow("thresh image",thresh_img)
cv2.waitKey(0)


