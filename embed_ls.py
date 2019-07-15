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

msg = args["message_text"]
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
i=1
for a, b in zip(c_img, msg_int):
    a = np.binary_repr(a, width=8)
   
    # step 3: perform XOR operations on the 7th and on the 6th bit    
    xor_a = int(a[1]) ^ int(a[2])
        
    # step 4: perform XOR operations on 8th bit with xor_a
    xor_b = int(a[0]) ^ xor_a
        
    # step 5: perform XOR operations on message bits with 3 MSB
    xor_c = int(b) ^ xor_b 
    
    
    # step 6: save xor_c, convert back to uint8
    
    #print("ln",ln)
    save = a[:-1] + str(xor_c)
    
   # print("steg: ",i,save)   
        
    out.append(int(save, 2))
    i=i+1
    
stego_img = np.array(out)
stego_img = np.reshape(stego_img, (256, 256))
print("Steganography Succeded!")
cv2.imwrite("stego_image.png", stego_img)



    
