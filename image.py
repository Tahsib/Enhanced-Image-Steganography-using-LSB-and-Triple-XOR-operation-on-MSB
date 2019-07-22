import cv2

im = cv2.imread("lena.png",0)
im1 = cv2.imread("stego_image.png",0)
im2 = cv2.imread("stego_image1.png",0)

print(im[0][0],im[0][1],im[0][2],im[0][3],im[0][4],im[0][5],im[0][6],im[0][7])
print(im1[0][0],im1[0][1],im1[0][2],im1[0][3],im1[0][4],im1[0][5],im1[0][6],im1[0][7])
print(im2[0][0],im2[0][1],im2[0][2],im2[0][3],im2[0][4],im2[0][5],im2[0][6],im2[0][7])
