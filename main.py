import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Generate qrcode
content = input("Give the text:")
qrgennerate = pyqrcode.create(content)
qrgennerate.png("content.png", scale=8)

# scan the qrcode
qr1 = decode(Image.open("content.png"))
print(qr1[0].data.decode('ascii'))
