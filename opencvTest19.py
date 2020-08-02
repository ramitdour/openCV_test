#https://www.youtube.com/watch?v=aDY4aBLFOIg&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=21
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

#img = cv.imread('opencv-logo.png',-1)
img = cv.imread('data/sudoku.png',0)

#Laplacian Gradient 
lap = cv.Laplacian(img , cv.CV_64F ,ksize = 3)
lap = np.uint8(np.absolute(lap))

#sobel
sobelX = cv.Sobel(img ,  cv.CV_64F , 1 , 0,ksize = 3)
sobelY = cv.Sobel(img ,  cv.CV_64F , 0 , 1,ksize = 3)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined  = cv.bitwise_or(sobelX,sobelY)


titles = ['image' ,'Laplacian' ,'sobelX' , 'sobelY' ,'sobelCombined']
images = [img ,lap ,sobelX , sobelY,sobelCombined]

dictgrid = {1:(1,1) , 2:(1,2) , 3:(1,3), 4:(2,2), 5:(2,3), 6:(2,3), 7:(4,2) ,8:(4,2), 9:(3,3), 10:(3,4)}
l = len(titles)

for i in range(l):
    plt.subplot(*dictgrid[l],i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

