import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# for j in events:
#     print(j)

def nothing(x):
    pass

img = np.zeros((300,515,3),np.uint8)
# img = cv.imread('lenna.jpg')

cap = cv.VideoCapture(0)

cv.namedWindow('Tracking')
cv.createTrackbar('LH','Tracking',0,255,nothing)
cv.createTrackbar('LS','Tracking',0,255,nothing)
cv.createTrackbar('LV','Tracking',0,255,nothing)
cv.createTrackbar('UH','Tracking',255,255,nothing)
cv.createTrackbar('US','Tracking',255,255,nothing)
cv.createTrackbar('UV','Tracking',255,255,nothing)



cv.createTrackbar('CP','image',10,400,nothing)


switch = 'color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)


while(1):
    #frame = cv.imread('smarties.png')
    _,frame = cap.read()
    
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    #l_b = np.array([110,50,50])
    l_h = cv.getTrackbarPos('LH','Tracking')
    l_s = cv.getTrackbarPos('LS','Tracking')
    l_v = cv.getTrackbarPos('LV','Tracking')
    
    u_h = cv.getTrackbarPos('UH','Tracking')
    u_s = cv.getTrackbarPos('US','Tracking')
    u_v = cv.getTrackbarPos('UV','Tracking')
    
#     l_b = np.array([110,50,50])
#     u_b = np.array([130,255,255])
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    
    mask = cv.inRange(hsv,l_b,u_b)
    
    res = cv.bitwise_and(frame,frame,mask=mask)
    
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    k = cv.waitKey(1) & 0xFF
    
    
    if k == 27:
        break

    
pass


# cv.imshow('img1',img1)
# cv.imshow('img2',img2)
# cv.waitKey(0)
cap.release()
cv.destroyAllWindows()
