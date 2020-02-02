# -*- coding: utf-8 -*-

import cv2
import argparse
import numpy as np
import binascii

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--stego_image", required=True,
                help="path to stego image")

args = vars(ap.parse_args())

def bin2str(binary):
    message = binascii.unhexlify('%x' % (int('0b'+binary, 2)))
    return message

# step 1: read stego image
stego_img = cv2.imread(args["stego_image"], 0)

# step 2: change pixel value to binary
stego_flatten = stego_img.flatten()
#stego_flatten = [np.binary_repr(x, width=8) for x in stego_flatten]

out = ""
#out = []
for x in stego_flatten:
    x = np.binary_repr(x, width=8)

    xor_c = int(x[-1]) 
    out += str(xor_c)
    if out[-16:] == '1111111111111110':
        break
    xor_c = int(x[-2]) 
    out += str(xor_c)
    if out[-16:] == '1111111111111110':
        break
msg = bin2str(out[:-16])
print(msg.decode())

