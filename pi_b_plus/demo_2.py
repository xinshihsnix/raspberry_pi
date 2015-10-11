import cv2
from utils import time_now_str

cameraCapture = cv2.VideoCapture(0)

fps = 1     # an assumption

CAMERA_WIDTH = int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
CAMERA_HEIGHT = int(cameraCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

size = (
    int(CAMERA_WIDTH/2),
    int(CAMERA_HEIGHT/2),
    )

video_name = time_now_str() + '_start' + '.avi'
videoWriter = cv2.VideoWriter(video_name, cv2.cv.CV_FOURCC('I','4','2','0'), fps, size)

success, frame = cameraCapture.read()

numFramesRemaining = 10 * fps - 1
# numFramesRemaining = 2 * fps - 1

while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1

cameraCapture.release()
