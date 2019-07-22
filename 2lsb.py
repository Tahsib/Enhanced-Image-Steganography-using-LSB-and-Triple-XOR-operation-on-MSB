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
print(c_img)

print("Cover Image Size after flatten",c_img.size)

def str2bin(message):
    binary = bin(int(binascii.hexlify(bytes(message, 'UTF-8')), 16))
    return binary[2:]

with open(args["message_text"],"r") as f:
    msg = f.read().strip()
    

#msg = args["message_text"]
binary = str2bin(msg) + '1111111111111110'
bina = len(str2bin(msg))
bin_len = len(binary)

if bin_len % 2 == 0:
    k = 0
else:
    k = 1
print(f"k = {k}")

print("bin",bina)
print("bin_len",bin_len)

'''
extra_len= img_size - bin_len
print("extra_len",extra_len)
for i in range(extra_len):
    if (i % 2) == 0:
        binary+=str(1)
    else:
        binary+=str(0)

'''
b_list = [] #for making "binary" sting the list
for item in binary:
    b_list.append(item)

#making the binary list numpy array
b_arr = np.array(b_list)
b_int = b_arr.astype(np.int)
msg_int = b_int

b=b_int
print("Text in binary size",msg_int.size)
out = []

l=0
for a in (c_img):
    if l< bin_len:
        a = np.binary_repr(a, width=8)
        #xor_a = int(a[1]) ^ int(a[2])
        #xor_b = int(a[0]) ^ xor_a    

        xor_c1 = int(b[l])
        l=l+1
        a1 = str(xor_c1)

        if k == 1:
            if l == (bin_len):
                save = a[:-1] + a1
                out.append(int(save, 2))
                continue

        xor_c2 = int(b[l])
        l=l+1
        a2 = str(xor_c2)     
        save = a[:-2] + a2 + a1
        out.append(int(save, 2))
        
    else:
        save = a
        out.append(save)
'''
for a, b in zip(c_img, msg_int):
    a = np.binary_repr(a, width=8)
    if bin_len!=0:   
    # step 3: perform XOR operations on the 7th and on the 6th bit    
        xor_a = int(a[1]) ^ int(a[2])
        
    # step 4: perform XOR operations on 8th bit with xor_a
        xor_b = int(a[0]) ^ xor_a
        
    # step 5: perform XOR operations on message bits with 3 MSB
        xor_c = int(b) ^ xor_b 
    
    
    # step 6: save xor_c, convert back to uint8
        save = a[:-1] + str(xor_c)
        bin_len = bin_len - 1
    else:
        save = a  
        
    out.append(int(save, 2))
'''   
    
stego_img = np.array(out)
stego_img = np.reshape(stego_img, (256, 256))
print("Steganography Succeded!")
cv2.imwrite("2lsb.png", stego_img)



    
