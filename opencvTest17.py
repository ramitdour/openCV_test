import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread('smarties.png',0)

_,th1 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY)
_,mask = cv.threshold(img , 220 , 255 , cv.THRESH_BINARY_INV)

kernal = np.ones((5,5),np.uint8)

dilation = cv.dilate(mask,kernal , iterations = 3)
erosion = cv.erode(mask,kernal,iterations = 5)
# Erosion + dialation 
opening = cv.morphologyEx(mask , cv.MORPH_OPEN , kernal)
#  Dialation + Erosion
closing = cv.morphologyEx(mask , cv.MORPH_CLOSE , kernal)

mg = cv.morphologyEx(mask , cv.MORPH_GRADIENT , kernal)
th = cv.morphologyEx(mask , cv.MORPH_TOPHAT , kernal)

_,th3 = cv.threshold(img , 220 , 255 , cv.THRESH_MASK)
_,th4 = cv.threshold(img , 127 , 255 , cv.THRESH_OTSU)
_,th5 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO)
_,th6 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO_INV)
_,th7 = cv.threshold(img , 127 , 255 , cv.THRESH_TRIANGLE)
_,th8 = cv.threshold(img , 127 , 255 , cv.THRESH_TRUNC)

titles = ['img','mask','dilation','erosion','opening','closing','mg','th']
images = [img , mask ,dilation ,erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

# img = cv.imread('lena.jpg',-1)
# cv.imshow('image',img)
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


# plt.imshow(img)

#hide the xy labels
# plt.xticks([]),plt.yticks([])

plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()
