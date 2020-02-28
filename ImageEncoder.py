from PIL import Image


im = Image.open('AppIcon.JPG').convert("RGBA") # Can be many different formats.
pix = im.load()

im2 = Image.new("RGB", im.size)
pixelsNew = im2.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixelsNew[i, j] = (0, 255, 0, 255)

test_str = "TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!TUNA Needs to stop running around nowwwwww!!!!!!!!!!!!!!"
res = ''.join(format(ord(i), 'b') for i in test_str) 
print("The string after binary conversion : " + str(res)) 

def convertToInt(binaryVal):
    if binaryVal == "00":
        return 0
    elif binaryVal == "01":
        return 1
    elif binaryVal == "10":
        return 2
    elif binaryVal == "11":
        return 3

def getNewValue(initialVal, res, i):
    # print(i, "i value")
    #print(initialVal, " before shift")
    initialVal >>=  2  
    #print(initialVal, " after shift right")
    initialVal <<= 2
    #print(initialVal, " after shift left")
    initialVal += convertToInt(res[i: i+2])
    #print(initialVal, " after insertion")
    return initialVal

def insertMessage(binaryMessage):
    for i in range(len(binaryMessage)//6):
        colorR = pixelsNew[0, i][0]
        print(colorR, "colorR")
        colorG = pixelsNew[0, i][1]
        print(colorG, "colorG")
        colorB = pixelsNew[0, i][2]
        print(colorB, "colorB")
        
        newR = getNewValue(colorR, binaryMessage, (i * 6))
        print(newR, "newR")
        newG = getNewValue(colorG, binaryMessage, (i * 6) + 2)
        print(newG, "newG")
        newB = getNewValue(colorB, binaryMessage, (i * 6) + 4)
        print(newB, "newB")
        print(res[i*6:(i+1)*6])
        print('')

def decryptMessage(pixelArray):
    

print("The original string is : " + str(test_str)) 


im2.show()



