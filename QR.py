import qrcode
import cv2

img=qrcode.make(r"C:\Users\AMRIX\Downloads\q.jpg")
img.save(r"E:\coding\open cv\murtaza\q.jpg")

d=cv2.QRCodeDetector()
val,points,straight_qrcode=d.detectAndDecode(cv2.imread(r"E:\coding\open cv\murtaza\q.jpg"))
print(val)

