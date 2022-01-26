far = input("fahrenheit: ")
try:
    far = int(far)
    cels = (far - 32) * 5 / 9
    print("fahrenheit: " + str(far) + "    celsius: " + str(cels))
except:
    print("invalid input")

cel = input("celsius: ")
try:
    cel = int(cel)
    fahr = (cel * (9/5)) + 32
    print("celsius: " + str(cel) + "   fahrenheit: " + str(fahr))
except:
    print("invalid input")
