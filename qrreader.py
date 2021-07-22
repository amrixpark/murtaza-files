import pyqrcode

from pyzbar.pyzbar import decode
from PIL import Image

qr=pyqrcode.create("https://youtu.be/5Q7zZzhHP6s")
qr.png(r"E:\a.png",scale=8)

d=decode(Image.open(r"E:\a.png"))
print(d[0].data.decode("ascii"))