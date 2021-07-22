import cv2

z=cv2.CascadeClassifier(r"C:\Users\AMRIX\Downloads\facecascade.xml")
img=cv2.imread(r"C:\Users\AMRIX\Downloads\img downloaded\girlz.jpg")
img=cv2.resize(img,(800,500))
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
k=z.detectMultiScale(img,1.5,4)

for (x,y,w,h) in k:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

cv2.imshow("result",img)
cv2.waitKey(0)
