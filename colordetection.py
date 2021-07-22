import cv2

import numpy as np

img=cv2.imread(r"C:\Users\AMRIX\Downloads\team.jpg")
img=cv2.resize(img,(400,300))
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
blur=cv2.GaussianBlur(img,(7,7),0)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(img,120,120)

display=np.vstack((img,hsv,blur,))
cv2.imshow("display",display)
cv2.imshow("canny",canny)
cv2.imshow("gray",gray)

cv2.waitKey(0)