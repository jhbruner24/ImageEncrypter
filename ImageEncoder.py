from PIL import Image



#Creates image
im = Image.new("RGB", (1024,1024))
pixelsNew = im.load()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixelsNew[i, j] = (0, 255, 0, 255)

messageToInsert = "TUNA Needs to stop running!!!!TUNA Needs to stop running!!!!TUNA Needs to stop running!!!!"

def convertMessageToBinary(stringToConvert):
    res = ''.join(format(ord(i), 'b') for i in stringToConvert) 
    print("The message after binary conversion : " + str(res))
    return res

def convertToInt(binaryVal):
    if binaryVal == "00":
        return 0
    elif binaryVal == "01":
        return 1
    elif binaryVal == "10":
        return 2
    elif binaryVal == "11":
        return 3

def getNewRGBValue(initialVal, res, i):
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
    #Iterate through each bit in Message
    for i in range(len(binaryMessage)//6):
        colorR = pixelsNew[0, i][0]
        print(colorR, "colorR")
        colorG = pixelsNew[0, i][1]
        print(colorG, "colorG")
        colorB = pixelsNew[0, i][2]
        print(colorB, "colorB")

        #Assign RGB values
        newR = getNewRGBValue(colorR, binaryMessage, (i * 6))
        print(newR, "newR")
        newG = getNewRGBValue(colorG, binaryMessage, (i * 6) + 2)
        print(newG, "newG")
        newB = getNewRGBValue(colorB, binaryMessage, (i * 6) + 4)
        print(newB, "newB")
        print(binaryMessage[i*6:(i+1)*6])
        print('')

def decryptMessage(pixelArray):
    pass

insertMessage(convertMessageToBinary(messageToInsert))

im.show()



