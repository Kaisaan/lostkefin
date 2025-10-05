import sys

anmFile = open(f"{sys.argv[1]}", "r+b")
binFile = open(f"{sys.argv[2]}", "rb")
offset = int(sys.argv[3], 16)

binData = binFile.read()
#print(binData)

anmFile.seek(offset)
anmFile.write(binData)

