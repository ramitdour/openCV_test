import cv2 as cv
import datetime
#print(cv.__version__)

cap = cv.VideoCapture(0)
#cap = cv.VideoCapture('movie.avi')

print('w=',cap.get(cv.CAP_PROP_FRAME_WIDTH),
        'h=',cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# cap.set(3,1208)
# cap.set(4,720)
# 
# print('w=',cap.get(3),
#         'h=',cap.get(4))




while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret :
        print('w=',cap.get(cv.CAP_PROP_FRAME_WIDTH),
        'h=',cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        
        
        
        font = cv.FONT_HERSHEY_COMPLEX
        text = 'w=' + str(cap.get(3))+',h='+str(cap.get(4))
        text = datetime.datetime.now().__str__() 
        frame = cv.putText(frame,text,(10,50),font,1,(0,255,255),1,cv.LINE_AA)

        
       
        
        #gray = cv.cvtColor(frame , cv.COLOR_BGR2GRAY)
        
        cv.imshow('video feed frame', frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
    
cap.release()

cv.destroyAllWindows()