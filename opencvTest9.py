import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# for j in events:
#     print(j)

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
#img2 = cv.imread('image_1.png')
img2 = cv.rectangle(np.zeros((250,500,3),np.uint8),(0,0),(250,250),(255,255,255),-1)

bitAnd = cv.bitwise_and(img1,img2)
cv.imshow('bitAnd',bitAnd)
#and ,or, not ,xor


cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.waitKey(0)
cv.destroyAllWindows()
