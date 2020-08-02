import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# for j in events:
#     print(j)


def click_event(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
       
        cv.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if(points.__len__() >= 2):
            cv.line(img,points[-1],points[-2],(255,0,0),5)
            
        cv.imshow('image',img)
    
    if event == cv.EVENT_RBUTTONDOWN:
        blue =  img[x,y,0]
        green =  img[x,y,1]
        red =  img[x,y,2]
        font = cv.FONT_HERSHEY_COMPLEX
        text = str(blue)+','+str(green)+','+str(red)
        cv.putText(img,text,(x,y),font,0.5,(0,255,255),1)
        cv.imshow('image',img)
        
img = np.zeros([512,512,3],np.uint8)
img = cv.imread('lena.jpg',-1)
cv.imshow('image',img)

points = []

cv.setMouseCallback('image',click_event )


cv.waitKey(0)
cv.destroyAllWindows()