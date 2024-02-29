 
# Python code to read image
import cv2
 
img = cv2.imread("bird.png", cv2.IMREAD_COLOR)
 
half = cv2.resize(img, (0, 0), fx = 0.01, fy = 0.01)
cv2.imshow("image", img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()