from PIL import Image
import math, binascii

class ImageProcessor:
    #dictionaries for processing bits
    convertStringToInt = {"00": 0, "01": 1, "10": 2, "11": 3}
    convertIntToString = {0: "00", 1: '01', 2: '10', 3: '11'}

    def __init__(self, file_name_in="Mason.jpeg"):
        # print(file_name_in)
        self.file_name = file_name_in
        #opens image
        self.im = Image.open(file_name_in)
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
        picture_length, picture_width = self.im.size
        for i in range(math.ceil(len(binaryMessage)/6)):

            row = i / picture_width
            col = i % picture_width

            colorR = self.pixelsNew[row, col][0]
            # print(colorR, "colorR")
            colorG = self.pixelsNew[row, col][1]
            # print(colorG, "colorG")
            colorB = self.pixelsNew[row, col][2]
            # print(colorB, "colorB")

            #Assign RGB values
            newR = self.getNewRGBValue(colorR, binaryMessage, (i * 6))
            # print(newR, "newR")
            newG = self.getNewRGBValue(colorG, binaryMessage, (i * 6) + 2)
            # print(newG, "newG")
            newB = self.getNewRGBValue(colorB, binaryMessage, (i * 6) + 4)

            self.pixelsNew[row, col] = (newR, newG, newB, 255)

            # print(newB, "newB")
            # print(binaryMessage[i*6:(i+1)*6])
            # print('')


    def decryptMessage(self, width=200, height=1):
        if (height > self.get_size()[0]):
            height = self.get_size()[0]
        if (width > self.get_size()[1]):
            width = self.get_size()[1]

        pixelArray = self.im.load()

        binaryString = ""
        for k in range(height):
            for i in range(width): #should be 1024 for this file, but I truncated
                for j in range(3):
                    binaryString += self.convertIntToString[pixelArray[k, i][j] % 4]
        # print(binaryString)

        # n = int('0b' + binaryString, 2)
        # print("decryptMessage:", n.to_bytes((n.bit_length() + 7) // 8, 'big').decode())
        print("decryptMessage:", self.bits2string(binaryString))

    def get_size(self):
        return self.im.size

    def show(self):
        self.im.show()


# INSERT STRING IMAGE FILE NAME HERE
image_file_name = "Mason.jpeg"

# You may either insert a message as a string or read from another file
# INSERT STRING MESSAGE HERE
message = "Hey you! Yeah, you! This is pretty cool, huh!"
# INSERT MESSAGE AS FILE
with open('book.txt', 'r') as file:
    data = file.read().replace('\n', ' ').replace('\’', "").replace('-', "*dash*").replace('–', "*dash*")

im_proc = ImageProcessor(image_file_name)

print("data", data, "\n")

message = data
im_proc.insertAndShow(message)

picture_length, picture_width = im_proc.get_size()
im_proc.decryptMessage(picture_width, 1)
