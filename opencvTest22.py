#https://www.youtube.com/watch?v=HfM9s2ehErE&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=25

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt 

for j in range(1,11):
    
    #img = cv.imread('opencv-logo.png',-1)
    levels = j
    apple = cv.imread('data/apple.jpg',-1)
    orange = cv.imread('data/orange.jpg',-1)
    print(apple.shape)
    print(orange.shape)
    
    apple_orange = np.hstack((apple[:, :256] , orange[: , 256:]))
    
    # generte gaussian pyramid for apple 
    apple_copy = apple.copy()
    gp_apple = [apple_copy]
    
    for i in range(levels):
        apple_copy = cv.pyrDown(apple_copy)
        gp_apple.append(apple_copy)
        
    # generte gaussian pyramid for orange 
    orange_copy = orange.copy()
    gp_orange = [orange_copy]
    
    for i in range(levels):
        orange_copy = cv.pyrDown(orange_copy)
        gp_orange.append(orange_copy)
        
    # generate laplacian pyramid for apple
    apple_copy = gp_apple[levels - 1 ].copy()
    lp_apple = [apple_copy]
    
    for i in range(levels-1 , 0 , -1):
        gaussian_expanded = cv.pyrUp(gp_apple[i])
        laplacian  = cv.subtract(gp_apple[i-1] , gaussian_expanded)
        lp_apple.append(laplacian)
        
    # generate laplacian pyramid for apple
    orange_copy = gp_apple[levels - 1 ].copy()
    lp_orange = [orange_copy]
    
    for i in range(levels-1 , 0 , -1):
        gaussian_expanded = cv.pyrUp(gp_orange[i])
        laplacian  = cv.subtract(gp_orange[i-1] , gaussian_expanded)
        lp_orange.append(laplacian)
        
    # now add left and right  halves of images in each level
    apple_orange_pyramid = []
    n = 0
    
    for apple_lap,orange_lap in zip(lp_apple,lp_orange):
        n += 1 
        cols, rows , ch  = apple_lap.shape
        
        laplacian = np.hstack((apple_lap[:,:int(cols/2)], orange_lap[:,int(cols/2):]))
        apple_orange_pyramid.append(laplacian)
        
    #now reconstruct the img 
    apple_orange_reconstruct = apple_orange_pyramid[0]
    
    for i in range(1,levels):
        apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
        apple_orange_reconstruct = cv.add(apple_orange_pyramid[i] , apple_orange_reconstruct)
    
        
        
    
           
        
    
    # cv.imshow('apple',apple)
    # cv.imshow('orange',orange)
    # cv.imshow('apple_orange',apple_orange)
    cv.imshow('apple_orange_reconstruct_'+str(j),apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()
