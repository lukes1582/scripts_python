'''
Created on 8 mag 2020

@author: lukes158@gmail.com l0m1s Luca Vidoni
'''

print ("***************")
print ("@lukes1582")
print ("***************")

import cv2

img = cv2.imread('images/input.jpg')

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Canale H', hsv_img[:, :, 0])
cv2.imshow('Canale S', hsv_img[:, :, 1])
cv2.imshow('Canale V', hsv_img[:, :, 2])

cv2.waitKey()
