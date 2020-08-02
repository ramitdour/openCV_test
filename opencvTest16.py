import cv2 as cv
#import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread('gradient.png',0)
_,th1 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY)
_,th2 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img , 127 , 255 , cv.THRESH_MASK)
_,th4 = cv.threshold(img , 127 , 255 , cv.THRESH_OTSU)
_,th5 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO)
_,th6 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO_INV)
_,th7 = cv.threshold(img , 127 , 255 , cv.THRESH_TRIANGLE)
_,th8 = cv.threshold(img , 127 , 255 , cv.THRESH_TRUNC)

titles = ['img','THRESH_BINARY','THRESH_BINARY_INV','THRESH_MASK',
          'THRESH_OTSU','THRESH_TOZERO','THRESH_TOZERO_INV',
          'THRESH_TRIANGLE','THRESH_TRIANGLE']
images = [img , th1 , th2 , th3 , th4 , th5 , th6 , th7 , th8]

for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])

# img = cv.imread('lena.jpg',-1)
# cv.imshow('image',img)
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


# plt.imshow(img)

#hide the xy labels
# plt.xticks([]),plt.yticks([])

plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()
