import cv2 as cv
import numpy as np

img = cv.imread('gradient.png',0)
_,th1 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY)
_,th2 = cv.threshold(img , 127 , 255 , cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img , 127 , 255 , cv.THRESH_MASK)
_,th4 = cv.threshold(img , 127 , 255 , cv.THRESH_OTSU)
_,th5 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO)
_,th6 = cv.threshold(img , 127 , 255 , cv.THRESH_TOZERO_INV)
_,th7 = cv.threshold(img , 127 , 255 , cv.THRESH_TRIANGLE)
_,th8 = cv.threshold(img , 127 , 255 , cv.THRESH_TRUNC)

cv.imshow('Image',img)
cv.imshow('THRESH_BINARY',th1)
cv.imshow('THRESH_BINARY_INV',th2)
# cv.imshow('THRESH_MASK',th3)
# cv.imshow('THRESH_OTSU',th4)
cv.imshow('THRESH_TOZERO',th5)
cv.imshow('THRESH_TOZERO_INV',th6)
cv.imshow('THRESH_TRIANGLE',th7)
cv.imshow('THRESH_TRUNC',th8)



cv.waitKey(0)
cv.destroyAllWindows()
