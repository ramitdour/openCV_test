import cv2 as cv

#print(cv.__version__)

img = cv.imread('lena.jpg',0)
print(img)
cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF
if(k == 27):
    cv.destroyAllWindows()
elif (k == ord('s')):
    cv.imwrite('lena_copy1.png',img)