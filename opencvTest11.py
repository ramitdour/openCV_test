import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# for j in events:
#     print(j)

def nothing(x):
    print(x)

img = np.zeros((300,515,3),np.uint8)
# img = cv.imread('lenna.jpg')
cv.namedWindow('image')

cv.createTrackbar('CP','image',10,400,nothing)


switch = 'color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)


while(1):
    img = cv.imread('lena.jpg')
#     cv.imshow('image',img)
    pos = cv.getTrackbarPos('CP','image',)
    font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv.putText(img,str(pos),(50,150),font,4,(0,0,255))
    
    k = cv.waitKey(1) & 0xFF
    
    
    if k == 27:
        break
    
    
   
    s = cv.getTrackbarPos(switch,'image',)
    
    if s == 0:
        #img[:] = 0
        pass
    else:
        #img[:] = [b,g,r]
        img = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        
    cv.imshow('image',img)

# cv.imshow('img1',img1)
# cv.imshow('img2',img2)
# cv.waitKey(0)
cv.destroyAllWindows()
