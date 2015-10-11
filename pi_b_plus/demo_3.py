import cv2

cv2.namedWindow('Video')

capture = cv2.VideoCapture(r'xxx.avi')
_, frame = capture.read()
while frame is not None:
    cv2.imwrite('screenshot.bmp', frame)