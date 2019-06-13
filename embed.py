import cv2
import numpy as np
import binascii
import itertools
import operator


c_img = cv2.imread('le.png',0)
print("c_size bef",c_img.size)
c_img = cv2.resize(c_img,(256,256))

s_ize = 256*256
c_img = c_img.flatten()

print("c_size af",c_img.size)

def str2bin(message):
    binary = bin(int(binascii.hexlify(bytes(message, 'UTF-8')), 16))
    return binary[2:]

msg = "oper"
binary = str2bin(msg) + '1111111111111110'

ln = len(binary)
print("prim_ln",ln)

cur_len= s_ize - ln
print("cur_len",cur_len)
for i in range(cur_len):
    if (i % 2) == 0:
        binary+=str(1)
    else:
        binary+=str(0)

b_list = [] #
for item in binary:
    b_list.append(item)


b_arr = np.array(b_list)
b_int = b_arr.astype(np.int)
msg_int = b_int
print("c_img",c_img.size)
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



    
