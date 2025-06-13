import unicodedata

length = 0
counter = 0
string = ''

colours = {"[GREEN]":"#gr", "[WHITE]":"#wh"}

print("Type/Paste your text and then Enter")

while (line := input()):
    string += line

#string = (input("Enter a string ").replace('\n', " "))

for key in colours.keys():
    string = string.replace(key, colours[key])

print(string)

length = len(string)

#for char in string:
#    status = unicodedata.east_asian_width(char)
#    if status == 'F':
#         print(char)
#         length += 1

# length = length + string.count(",")

counter = string.count("[PAUSE]")

if (counter > 0):
    print(f"{counter} pause")
    length = length - (counter * 5)
    counter = 0

counter = string.count("<")

if (counter > 0):
    print(f"{counter} <")
    length = length - (counter * 4)
    counter = 0

counter = string.count("[LINE]")

if (counter > 0):
    print(f"{counter} line")
    length = length - (counter * 5)
    counter = 0

counter = string.count("[WAIT]")

if (counter > 0):
    print(f"{counter} wait")
    length = length - (counter * 4)
    counter = 0


char = chr(length)

print(f"The string will have a converted length of {length} in hex is {length:X} its character is {char}")