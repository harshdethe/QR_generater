#Import Library
import time
import qrcode
#Generate QR Code
img=qrcode.make('https://github.com/harshdethe')
img.save('github.png')