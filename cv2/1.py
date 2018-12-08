import cv2

#choose the camera

while(True):
  #capture the image
  #show the image
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
