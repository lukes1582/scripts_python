'''
Created on 8 mag 2020

@author: lukes158@gmail.com l0m1s Luca Vidoni
'''

print ("***************")
print ("@lukes1582")
print ("***************")

import cv2

img = cv2.imread('images/input.jpg')

yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

cv2.imshow('Canale Y', yuv_img[:, :, 0])
cv2.imshow('Canale U', yuv_img[:, :, 1])
cv2.imshow('Canale V', yuv_img[:, :, 2])

cv2.waitKey()
