import cv2

img = cv2.imread("C:\\Users\\asus\\Pictures\\Camera Roll\\IMG_4150.jpg")
res=cv2.resize(img,(640,640),interpolation=cv2.INTER_CUBIC)  
cv2.namedWindow("Image") 
cv2.imshow("Image", res) 
cv2.waitKey (0)  
cv2.destroyAllWindows()
