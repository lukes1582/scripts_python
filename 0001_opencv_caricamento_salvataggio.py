'''
Created on 8 mag 2020

@author: lukes158@gmail.com l0m1s Luca Vidoni
'''

print ("***************")
print ("@lukes1582")
print ("***************")

import cv2
gray_img = cv2.imread('images/input.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('scala di grigi',gray_img)
cv2.waitKey()
