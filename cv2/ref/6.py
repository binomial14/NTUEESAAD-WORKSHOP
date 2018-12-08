import cv2

cap = cv2.VideoCapture(0)

while(1):
  ret, frame = cap.read()
  blur = cv2.blur(frame,(100,100))
  
  cv2.imshow('frame',blur)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
