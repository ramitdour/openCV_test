import cv2 as cv
#import numpy as np
from matplotlib import pyplot as plt 

img = cv.imread('lena.jpg',-1)
cv.imshow('image',img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


plt.imshow(img)

#hide the xy labels
plt.xticks([]),plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
