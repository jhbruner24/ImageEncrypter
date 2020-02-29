from PIL import Image
import math, binascii

convertStringToInt = {"00": 0, "01": 1, "10": 2, "11": 3}
convertIntToString = {0: "00", 1: '01', 2: '10', 3: '11'}

#Creates image
im = Image.open("Mason.jpeg")
pixelsNew = im.load()
# for i in range(im.size[0]):
#     for j in range(im.size[1]):
#         pixelsNew[i, j] = (0, 255, 0, 255)

messageToInsert = "Hi Mason! This is secret haha"
 # Needs to stop running!!!!TUNA Needs to stop running!!!!TUNA Needs to stop running!!!!"

def string2bits(s):
    return ''.join([bin(ord(x))[2:].zfill(8) for x in s])

def bits2string(b):
    all_bytes = []
    for i in range(0, len(b), 8):
        all_bytes += [b[i:i+8]]
    return ''.join([chr(int(x, 2)) for x in all_bytes])

def convertMessageToBinary(stringToConvert):
    # res = ''.join(format(ord(i), 'b') for i in stringToConvert)
    # res = bin(int.from_bytes(stringToConvert.encode(), 'big'))[2:] #cut off the 0b part
    res = string2bits(stringToConvert)
    # print("message converted into binary:", res)
    return res

def getNewRGBValue(initialVal, res, i):
    # print(i, "i value")
    #print(initialVal, " before shift")
    if (res[i: i+2] in convertStringToInt):
        initialVal >>=  2
        #print(initialVal, " after shift right")
        initialVal <<= 2
        #print(initialVal, " after shift left")
        initialVal += convertStringToInt[res[i: i+2]]
        #print(initialVal, " after insertion")
    return initialVal

def insertMessage(binaryMessage):
    #Iterate through each bit in Message
    for i in range(math.ceil(len(binaryMessage)/6)):
        colorR = pixelsNew[0, i][0]
        # print(colorR, "colorR")
        colorG = pixelsNew[0, i][1]
        # print(colorG, "colorG")
        colorB = pixelsNew[0, i][2]
        # print(colorB, "colorB")

        #Assign RGB values
        newR = getNewRGBValue(colorR, binaryMessage, (i * 6))
        # print(newR, "newR")
        newG = getNewRGBValue(colorG, binaryMessage, (i * 6) + 2)
        # print(newG, "newG")
        newB = getNewRGBValue(colorB, binaryMessage, (i * 6) + 4)

        pixelsNew[0, i] = (newR, newG, newB, 255)

        # print(newB, "newB")
        # print(binaryMessage[i*6:(i+1)*6])
        # print('')


def decryptMessage(pixelArray):
    binaryString = ""
    for i in range(200): #should be 1024 for this file, but I truncated
        for j in range(3):
            binaryString += convertIntToString[pixelArray[0, i][j] % 4]
    # print(binaryString)

    # n = int('0b' + binaryString, 2)
    # print("decryptMessage:", n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
    print("decryptMessage:", bits2string(binaryString))



insertMessage(convertMessageToBinary(messageToInsert))
decryptMessage(im.load())
im.show()
