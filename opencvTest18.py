import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread('opencv-logo.png',-1)
img = cv.imread('data/self2.jpg',-1)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
kernel = np.ones((5,5), np.float32 )/25
dst = cv.filter2D(img , -1 , kernel)
blur = cv.blur(img, (5,5))
gausianBlur = cv.GaussianBlur(img,(5,5),0)
medianBlur = cv.medianBlur(img,5) #kernal size shoud be odd , except 1  # b/w dots salt and pepper
#to keep images sharper , to preseve the border/edges 
bilateralFilter = cv.bilateralFilter(img, 9 , 75 ,75)



_,th1 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY)


titles = ['image' , '2D Convolution' , 'blur','gausianBlur' ,'medianBlur' ,'bilateralFilter']
images = [img , dst , blur,gausianBlur,medianBlur,bilateralFilter]

dictgrid = {1:(1,1) , 2:(1,2) , 3:(1,3), 4:(2,2), 5:(3,2), 6:(2,3), 7:(4,2) ,8:(4,2), 9:(3,3), 10:(3,4)}
l = len(titles)

for i in range(l):
    plt.subplot(*dictgrid[l],i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])



plt.show()

