import cv2
cap = cv2.VideoCapture(0)
while(True):
  ret, frame = cap.read()
  #convert the type of your video
  cv2.imshow('frame', video)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
