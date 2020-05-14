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

cv2.imshow('Immagin HSV', hsv_img)

cv2.waitKey()
