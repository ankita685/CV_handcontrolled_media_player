import cv2
import numpy as np

img_path = "./emr_day_2/images/gray_scale.png"
img  = cv2.imread(img_path)
gray_scale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gvb",gray_scale_img)

(h,w)=gray_scale_img.shape
for i in range(0,h):
    for j in range(0,w):
        # print(gray_scale_img[i,j])
        if gray_scale_img[i,j] > 50:
            gray_scale_img[i,j] = 255
        else:
            gray_scale_img[i,j] = 0
cv2.imshow("gray_scale_img",gray_scale_img)
cv2.waitKey(0)