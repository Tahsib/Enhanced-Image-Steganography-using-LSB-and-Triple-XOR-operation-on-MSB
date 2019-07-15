import cv2
import numpy as np
import binascii
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cover_image", required=True,
                help="path to cover image")
ap.add_argument("-m", "--message_text", required=True,
                help="input message text")
args = vars(ap.parse_args())

c_img = cv2.imread(args["cover_image"],0)
print("Cover Image Size before flatten",c_img.size)
c_img = cv2.resize(c_img,(256,256))

img_size = 256*256
c_img = c_img.flatten()

print("Cover Image Size after flatten",c_img.size)

def str2bin(message):
    binary = bin(int(binascii.hexlify(bytes(message, 'UTF-8')), 16))
    return binary[2:]

with open(args["message_text"],"r") as f:
    msg = f.read().strip()

#msg = args["message_text"]
binary = str2bin(msg) + '1111111111111110'

bin_len = len(binary)
print("bin_len",bin_len)

extra_len= img_size - bin_len
print("extra_len",extra_len)
for i in range(extra_len):
    if (i % 2) == 0:
        binary+=str(1)
    else:
        binary+=str(0)

b_list = [] #for making "binary" sting the list
for item in binary:
    b_list.append(item)

#making the binary list numpy array
b_arr = np.array(b_list)
b_int = b_arr.astype(np.int)
msg_int = b_int
print("Text in binary size",msg_int.size)
out = []

for a, b in zip(c_img, msg_int):
    a = np.binary_repr(a, width=8)
    if bin_len!=0:   

        xor_c = int(b) 
    
    # step 6: save xor_c, convert back to uint8
        save = a[:-1] + str(xor_c)
        bin_len = bin_len - 1
    else:
        save = a  
        
    out.append(int(save, 2))
    
    
stego_img = np.array(out)
stego_img = np.reshape(stego_img, (256, 256))
print("Steganography Succeded!")
cv2.imwrite("stego_image1.png", stego_img)



    
