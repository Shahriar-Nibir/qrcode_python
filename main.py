import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


content = input("Give the text:")
qrgennerate = pyqrcode.create(content)
qrgennerate.png("content.png", scale=8)
