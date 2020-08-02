#https://www.youtube.com/watch?v=aDY4aBLFOIg&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=21
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

#img = cv.imread('opencv-logo.png',-1)
#img = cv.imread('data/messi5.jpg',0)
imgPath = 'data/sudoku.png',0

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv.resize(image, dim, interpolation=inter)

# -------------tracking window-------------
def nothing(x):
    pass

cv.namedWindow('Tracking')
cv.createTrackbar('t1','Tracking',0,255,nothing)
cv.createTrackbar('t2','Tracking',0,255,nothing)
# cv.createTrackbar('t1','Tracking',0,255,nothing)
# cv.createTrackbar('t1','Tracking',0,255,nothing)

#---------------------------------------------------

#---------------------------------------------------------------------



# --------------------------------------------------------



#--------------------------------------

while(1):
    frame = cv.imread(*imgPath)
    #resizing img
    frame = ResizeWithAspectRatio(frame, width=1280)
    
    
    
    t1 = cv.getTrackbarPos('t1','Tracking')
    t2 = cv.getTrackbarPos('t2','Tracking')
    
    canny = cv.Canny(frame , t1 ,t2)
    
    cv.imshow('window',canny)
    
#     titles = ['image' , 'canny']
#     images = [frame , canny]
#     
#     dictgrid = {1:(1,1) , 2:(1,2) , 3:(1,3), 4:(2,2), 5:(2,3), 6:(2,3), 7:(4,2) ,8:(4,2), 9:(3,3), 10:(3,4)}
#     l = len(titles)
#     
#     for i in range(l):
#         plt.subplot(*dictgrid[l],i+1),plt.imshow(images[i],'gray')
#         plt.title(titles[i])
#         plt.xticks([]),plt.yticks([])
    
    
    
    k = cv.waitKey(1) & 0xFF
    
    
    if k == 27:
        break
    
    
    plt.show()

