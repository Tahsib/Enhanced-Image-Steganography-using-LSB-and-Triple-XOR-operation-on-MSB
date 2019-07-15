import matplotlib.pyplot as plt
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cover_image", required=True,
                help="path to cover image")

args = vars(ap.parse_args())

im = cv2.imread(args["cover_image"])
# calculate mean value from RGB channels and flatten to 1D array
vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)
plt.xlim([0,255])
plt.show()
