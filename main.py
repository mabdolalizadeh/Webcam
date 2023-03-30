import numpy as np
import cv2
import time

t0 = time.time()
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        t1 = time.time() - t0
        text = "Mohammad\nAbdolalizadeh\n" + str(round(t1,2))

        redChannel = frame.copy()
        redChannel[:,:,2] = 255

        invChannel = 255 - frame

        tempGrayChannel = frame.copy()
        tempGrayChannel = cv2.cvtColor(tempGrayChannel,cv2.COLOR_BGR2GRAY)
        grayChannel = np.ones((720,1280,3))
        grayChannel[:,:,0] = tempGrayChannel
        grayChannel[:,:,1] = tempGrayChannel
        grayChannel[:,:,2] = tempGrayChannel

        tempArray1 = np.concatenate([frame, redChannel], 1)
        tempArray2 = np.concatenate([invChannel, grayChannel], 1)

        image = np.concatenate([tempArray1,tempArray2], 0)
    

        cv2.putText(image, text, (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))
        cv2.imshow("Webcam", image)

        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()