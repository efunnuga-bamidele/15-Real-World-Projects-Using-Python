from pyzbar.pyzbar import decode
from PIL import Image

print("Welcome to QRcode reader tool")


img = Image.open("qrcode.png")
data = decode(img)

print("Your Secret Message is : ")
print(data[0].data.decode())

 