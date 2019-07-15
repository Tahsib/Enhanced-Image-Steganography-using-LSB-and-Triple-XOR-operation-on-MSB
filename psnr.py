import numpy 
import math
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c","--cover_img", required=True, help="path to cover image")
ap.add_argument("-s","--stego_img", required=True, help="path to stego image")

arg = vars(ap.parse_args())
cover_img = cv2.imread(arg["cover_img"],0)
stego_img = cv2.imread(arg["stego_img"],0)

cover_img = cv2.resize(cover_img,(256,256))
stego_img = cv2.resize(stego_img,(256,256))

def psnr(img1, img2):
    mse = numpy.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

d=psnr(cover_img,stego_img)
print("Psnr value is: ",d)
