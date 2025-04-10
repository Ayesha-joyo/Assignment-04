from pyzbar.pyzbar import decode
from PIL import Image

# Open the image
img = Image.open('D:/Quarter-3/25-Projects/QRCODE/files/myqrcode1.png')

# Decode the image
result = decode(img)

# Print the result in a readable format
for item in result:
    print(f"Data: {item.data.decode('utf-8')}")
