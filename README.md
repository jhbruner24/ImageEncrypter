# ImageEncrypter

Takes photos and hides (unencrypted) messages within them.
Takes in photos with hidden messages and outputs the message hidden within them (if the message is hidden with the same scheme).
Could be extended to also encrypt the messages.


Image Encrypter works by modifying the two least significant bits of the Red, Green, and Blue values of each pixel. Humans are then unable to detect the color changes in the images because the least significant bits do not drastically modify the colors or appearance of the image. 

Pseduo Code (Encoding):
1. The input message is converted to binary.
2. For each pixel in input image until we have reached the end of the input message:
Get the current pixel.
        Replace the last two bits of the R value with that of the next two bits in the string.
        Replace the last two bits of the G value with that of the next two bits in the string.
        Replace the last two bits of the B value with that of the next two bits in the string.
        
Pseduo Code (Decoding):
1. For each pixel in input image:
        Get the current pixel.
        Record the last two bits of the R.
        Record the last two bits of the G value with that of the next two bits in the string.
        Record the last two bits of the B value with that of the next two bits in the string.
2. Convert the binary message back into a string.
