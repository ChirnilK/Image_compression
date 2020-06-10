# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:53:22 2020

@author: chiharu
"""

import cv2
import sys

def compressOpencv(filename, n=2):
    
    img = cv2.imread(filename)

    if img is None:
        print("Failed to load image file.")
        sys.exit(1)
        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    height, width = img.shape
    # print("width: " + str(width))
    # print("height: " + str(height))
    # print("dtype : " + str(img.dtype))

    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    width = width//n
    height = height//n
    
    min_size=min(width, height)
    if min_size < 60:
        print('The size is too small. Please change the rate')
    
    else:    
        resized_img = cv2.resize(img,(width, height))
        # print("width: " + str(width))
        # print("height: " + str(height))
        
        # cv2.imshow("img", resized_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

#compressOpencv('tt.jpg', 16)       