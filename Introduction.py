import cv2
import os
img = cv2.imread("C:/Users/vijay/OneDrive/Desktop/OPEN CV/JTpVKUS.jpg")
cv2.imshow("Title",img)
cv2.waitKey(0)
img1 = cv2.imread(r"C:\Users\vijay\OneDrive\Desktop\OPEN CV\JTpVKUS.jpg",0)
cv2.imshow("Title",img1)
cv2.waitKey(10000)
PATH_FOLDER = r"C:\Users\vijay\OneDrive\Desktop\OPEN CV\Save_IMG'S"
os.chdir(PATH_FOLDER)
cv2.imwrite("Red Town View.jpg",img)
SPLIT,SPLIT1,SPLIT2 = cv2.split(img)
cv2.imshow("TITLE",SPLIT)
cv2.waitKey(2000)
cv2.imshow("TITLE",SPLIT1)
cv2.waitKey(2000)
cv2.imshow("TITLE",SPLIT2)
cv2.waitKey(2000)
print(SPLIT)