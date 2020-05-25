# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:29:24 2020

@author: chiharu
"""
import numpy as np
#import matplotlib.pyplot as plt
import cv2


class Image_compression:
    
    def __init__(self, filepath):

        img=cv2.imread(filepath,0)

        height, width = img.shape[0], img.shape[1] 

        if height % 2 !=0:
            img = img[:-1]
            print ('Image was uneven (width-wise) and has been trimmed!')
            
        if width %2 !=0:
            imgT = img.transpose()
            imgT = imgT[:-1]
            img = imgT.transpose()
            print ('Image was uneven (height-wise) and has been trimmed!')
        
        print('Image size is {}x{}'.format(img.shape[0],img.shape[1]))
    
        cv2.imwrite('trimmed_img.jpg', img)
        img=cv2.imread('trimmed_img.jpg',0)
     
        self.img = img
        self.height = self.img.shape[0]
        self.width = self.img.shape[1]
     
 

    def haar(sz):
    
        """This function creates the Haar-matrix."""
    
        out = np.zeros((sz, sz))
    
        j=0
        for i in range(int(sz/2)):
           
            out[i,j]=np.sqrt(2)/2
            out[i,j+1]=np.sqrt(2)/2
            j+=2
        
        j=0
        for i in range(int(sz/2), sz):
           
            out[i,j]=-np.sqrt(2)/2
            out[i,j+1]=np.sqrt(2)/2
            j+=2

        return out


    def compression(self):
               
        w_m=Image_compression.haar(self.height)
        w_t=Image_compression.haar(self.width).T
        comp=np.dot(np.dot(w_m,self.img),w_t)
    
        cv2.imwrite('compedImage.jpg', comp) 
        comp = comp.astype(np.uint8)             #change dtype to uint8 from float 64
        comp = cv2.imread('compedImage.jpg',0)
        cv2.imshow('compedImage.jpg',comp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  

        return comp

    def topLeft(self):
                
        """This function cuts the top-left fourth of the image"""
            
        comp_img = Image_compression.compression(self)

        img = np.array(comp_img[0:self.height//2, 0:self.width//2])
        cv2.imwrite('top_left.jpg', img)       
        
        img = img.astype(np.uint8)                #change dtype to uint8 from float 64
        img=cv2.imread('top_left.jpg',0)
        cv2.imshow('top_left.jpg',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
        

# test1=Image_compression('kvinna.jpg')
# test1.topLeft()
test2=Image_compression('goat.jpg')
test2.topLeft()
            
