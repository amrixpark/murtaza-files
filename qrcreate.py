import qrcode

#img=qrcode.make("https://www.youtube.com/watch?v=vPk-H7Cu9Lo")
#img.save("C:/Users/AMRIX/Downloads/toptenskills.jpg")

img=qrcode.make("anand is a good boy")
img.save("C:/Users/AMRIX/Downloads/anand.jpg")

import qrcode
import cv2

d=cv2.QRCodeDetector()
val,points,straight_qrcode=d.detectAndDecode(cv2.imread("C:/Users/AMRIX/Downloads/anand.jpg"))
print(val)


import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

img=pyqrcode.create("today")
img.png(r"E:\coding\open cv\murtaza\am.jpg", scale=8)

d=decode(Image.open(r"E:\coding\open cv\murtaza\am.jpg"))
print(d[0].data.decode("ascii"))