#https://www.youtube.com/watch?v=HfM9s2ehErE&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=25

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 


img = cv.imread('opencv-logo.png',-1)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


ret, thresh = cv.threshold(imgGray , 127 , 255 , 0)

contours , hierarchy  = cv.findContours(thresh , cv.RETR_TREE , cv.CHAIN_APPROX_NONE)
print('nos of countours = ', str(len(contours)))
#print(contours[0])

cv.drawContours(img, contours , 8 ,(0,255,0),3)



cv.imshow('img',img)
cv.imshow('imgGray',imgGray)
# cv.imshow('apple_orange',apple_orange)

cv.waitKey(0)
cv.destroyAllWindows()
