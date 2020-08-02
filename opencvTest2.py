import cv2 as cv

#print(cv.__version__)

cap = cv.VideoCapture(0)
#cap = cv.VideoCapture('movie.avi')
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))


while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret :
        print('w=',cap.get(cv.CAP_PROP_FRAME_WIDTH),
        'h=',cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)
        
        gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
        
        cv.imshow('video feed frame', gray)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
    
cap.release()
out.release()
cv.destroyAllWindows()