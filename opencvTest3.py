import cv2 as cv
import numpy as np
#print(cv.__version__)

#img = cv.imread('lena.jpg',-1)
img = np.zeros([512,512,3],np.uint8)
img = cv.line(img,(0,0),(255,255),(255,0,0),1) 
img = cv.arrowedLine(img,(0,100),(255,255),(0,255,0),2)
img = cv.rectangle(img ,(384,0),(510,128),(0,0,255),2)
img = cv.circle(img,(447,63),63,(0,255,0),-1)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img,'hello world',(10,500),font,5,(0,255,0),1,cv.LINE_AA)

print(img)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if(k == 27):
    cv.destroyAllWindows()
elif (k == ord('s')):
    cv.imwrite('lena_copy1.png',img)