import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# for j in events:
#     print(j)

def nothing(x):
    print(x)

img = np.zeros((300,515,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)

switch = '0:OFF \n 1:ON'
cv.createTrackbar(switch,'image',0,1,nothing)


while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    b = cv.getTrackbarPos('B','image',)
    g = cv.getTrackbarPos('G','image',)
    r = cv.getTrackbarPos('R','image',)
    s = cv.getTrackbarPos(switch,'image',)
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]


# cv.imshow('img1',img1)
# cv.imshow('img2',img2)
# cv.waitKey(0)
cv.destroyAllWindows()
