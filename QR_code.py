import qrcode
# pip install qrcode
# pip install pillow - A library for image processing
img = qrcode.make("https://google.com")
img.save("qr1.png")
