import cv2
img_path = "./emr_day_2/images/book_page.jpg"
img  = cv2.imread(img_path)
gray_scale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("img",img)
thresh_val,thresh_img = cv2.threshold(gray_scale_img,200,255,cv2.THRESH_OTSU)
print(thresh_val)
cv2.imshow("B/W filter",thresh_img)

cv2.waitKey(0)