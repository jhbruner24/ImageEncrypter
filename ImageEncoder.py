from PIL import Image
import math, binascii

class ImageProcessor:
    #dictionaries for processing bits
    convertStringToInt = {"00": 0, "01": 1, "10": 2, "11": 3}
    convertIntToString = {0: "00", 1: '01', 2: '10', 3: '11'}

    def __init__(self, file_name_in="Mason.jpeg"):
        print(file_name_in)
        self.file_name = file_name_in
        #opens image
        self.im = Image.open("Mason.jpeg")

        #stores pixel values
        self.pixelsNew = self.im.load()
        # for i in range(im.size[0]):
        #     for j in range(im.size[1]):
        #         pixelsNew[i, j] = (0, 255, 0, 255)

    def string2bits(self, s):
        return ''.join([bin(ord(x))[2:].zfill(8) for x in s])

    def bits2string(self, b):
        all_bytes = []
        for i in range(0, len(b), 8):
            all_bytes += [b[i:i+8]]
        return ''.join([chr(int(x, 2)) for x in all_bytes])

    def convertMessageToBinary(self, stringToConvert):
        # res = ''.join(format(ord(i), 'b') for i in stringToConvert)
        # res = bin(int.from_bytes(stringToConvert.encode(), 'big'))[2:] #cut off the 0b part
        res = self.string2bits(stringToConvert)
        # print("message converted into binary:", res)
        return res

    def getNewRGBValue(self, initialVal, res, i):
        # print(i, "i value")
        #print(initialVal, " before shift")
        if (res[i: i+2] in self.convertStringToInt):
            initialVal >>=  2
            #print(initialVal, " after shift right")
            initialVal <<= 2
            #print(initialVal, " after shift left")
            initialVal += self.convertStringToInt[res[i: i+2]]
            #print(initialVal, " after insertion")
        return initialVal

    def insertAndShow(self, message):
        self.insertMessage(message)
        self.show()

    def insertMessage(self, message):
        binaryMessage = self.convertMessageToBinary(message)

        #Iterate through each bit in Message
        for i in range(math.ceil(len(binaryMessage)/6)):
            colorR = self.pixelsNew[0, i][0]
            # print(colorR, "colorR")
            colorG = self.pixelsNew[0, i][1]
            # print(colorG, "colorG")
            colorB = self.pixelsNew[0, i][2]
            # print(colorB, "colorB")

            #Assign RGB values
            newR = self.getNewRGBValue(colorR, binaryMessage, (i * 6))
            # print(newR, "newR")
            newG = self.getNewRGBValue(colorG, binaryMessage, (i * 6) + 2)
            # print(newG, "newG")
            newB = self.getNewRGBValue(colorB, binaryMessage, (i * 6) + 4)

            self.pixelsNew[0, i] = (newR, newG, newB, 255)

            # print(newB, "newB")
            # print(binaryMessage[i*6:(i+1)*6])
            # print('')


    def decryptMessage(self, num_pix=200):
        pixelArray = self.im.load()

        binaryString = ""
        for i in range(num_pix): #should be 1024 for this file, but I truncated
            for j in range(3):
                binaryString += self.convertIntToString[pixelArray[0, i][j] % 4]
        # print(binaryString)

        # n = int('0b' + binaryString, 2)
        # print("decryptMessage:", n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
        print("decryptMessage:", self.bits2string(binaryString))

    def show(self):
        self.im.show()


im_proc = ImageProcessor("Mason2.jpeg")

# messageToInsert = "Hi Mason! This is my new secret haha"
# Needs to stop running!!!!TUNA Needs to stop running!!!!TUNA Needs to stop running!!!!"
# im_proc.insertMessage(messageToInsert)
# im_proc.show()
im_proc.insertAndShow("Hello, Mason! You are my world!")
im_proc.decryptMessage()
