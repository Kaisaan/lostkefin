import sys
from PIL import Image

filename = sys.argv[1]

graphic = Image.open(f"{filename}", "r")

filename = filename.rstrip(".png")


mode = graphic.mode
data = list(graphic.getdata())
print(mode)
#print(data)
print(len(data))

binData = b""
for i in range(len(data)):
    byte = data[i].to_bytes(1)
    binData = binData + byte

with open(f"{filename}.bin", "wb") as out:
    out.write(binData)