import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Twitter_OpenCV_segmentation/test/01a.png')
# cv2.imshow("image",image)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# COLOR FILTERING
# Original following button coordinates RGB : 24,83,121
# hsv_for these : [101,224,241]
#Define range lower = [H - 10,100,100]
# upper = [H + 10,255,255]

lower = np.array([90, 100, 100])
upper = np.array([111,255,255])
# MASKING
mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.imwrite('result.png', res)
resgray = cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)

# CONTOURS
contours, hierarchy = cv2.findContours(resgray,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# REJECTING CONTOURS with area < 10000, area of button is approx. 11000
contours1 = []  # newcontours
big = 10000
for i in contours:
    print(cv2.contourArea(i))
    if cv2.contourArea(i) > big:
        contours1.append(i)

# DRAWING CONTOURS

cv2.drawContours(image, contours1, -1, (0, 0, 255), 3)

# BOUNDINGBOX ACROSS CONTOURS
for i in contours1:
    rect = cv2.boundingRect(i)
    x, y, w, h = rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, 'Button Detected', (x + w + 10, y + h), 0, 0.3, (0, 255, 0))
    print("Coordinates:", x, x + w, y, y + h)

cv2.imshow("resgray", resgray)
cv2.imshow("final", image)  # FINAL IMAGE
cv2.imwrite('final.png',image)

# COORDINATES are printed below
