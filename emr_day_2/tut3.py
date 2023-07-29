import cv2
video_reader = cv2.VideoCapture(0)

while True:
    success, frame = video_reader.read()
    if not success :
        break
    cv2.imshow("MY Video",frame)
    key = cv2.waitKey(100)
    if key == ord('q'):
        break

video_reader.release()
cv2.destroyAllWindows()