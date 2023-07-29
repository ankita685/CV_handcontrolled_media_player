import cv2
import numpy as np

img_path = "./emr_day_2/images/sherlock_kid.png"
img  = cv2.imread(img_path)
w_img =np.full(img.shape ,[0,0,50] ,dtype=np.uint8)
cv2.imshow("IMAGE2",w_img)

new_img = img + w_img
cv2.imshow("NEW",new_img)
cv2.waitKey(0)