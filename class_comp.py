# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:29:24 2020

@author: chiharu
"""
import numpy as np
import cv2
import sys


class Image_compression:
    
    def __init__(self, filepath):
        
        img = cv2.imread(filepath)
        
        if img is None:
            print("Failed to load image file.")
            sys.exit(1)
                
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
        height, width = img.shape
        
        """Here,  makes sure that the image have an even number of pixels, else the haar-transform will not work.
        If the rows/columns of the image is odd then cut off the last row/column and save the image."""
               
        if height % 2 !=0:
            img = img[:-1]
            print ('Image was uneven (width-wise) and has been trimmed!')
            
        if width %2 !=0:
            imgT = img.transpose()
            imgT = imgT[:-1]
            img = imgT.transpose()
            print ('Image was uneven (height-wise) and has been trimmed!')
        
        
        height, width = img.shape
        print('Trimmed image size is {}x{}'.format(height, width))
        cv2.imwrite('Trimmed_img.jpg', img)
        img=cv2.imread('Trimmed_img.jpg',0)
     
        self.img = img
        self.height = height
        self.width = width
         


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
                
        
        """Here is the first dotproduct"""    
        comp1=np.dot(w_m,self.img)
        cv2.imwrite('first_dotproduct.jpg', comp1) 
        comp1 = comp1.astype(np.uint8)       #change dtype to uint8 from float 64
        comp1=cv2.imread('first_dotproduct.jpg',0)
        cv2.imshow('First dotproduct',comp1)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
    
    
        """Here is the second dotproduct"""
        comp2=np.dot(self.img,w_t)
        cv2.imwrite('second_dotproduct.jpg', comp2) 
        comp2 = comp2.astype(np.uint8)       #change dtype to uint8 from float 64
        comp1=cv2.imread('second_dotproduct.jpg',0)
        cv2.imshow('Second dotproduct',comp2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
        """Finally both dotproducts together"""
        comp=np.dot(np.dot(w_m,self.img),w_t)
        cv2.imwrite('compdImage.jpg', comp)
        comp = comp.astype(np.uint8)             #change dtype to uint8 from float 64
        comp = cv2.imread('compdImage.jpg',0)
        cv2.imshow('Compressed image',comp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  

        return comp

    def topLeft(self):
                
        """This function cuts the top-left fourth of the image"""
            
        comp_img = Image_compression.compression(self)

        img = np.array(comp_img[0:self.height//2, 0:self.width//2])
        cv2.imwrite('Top_left.jpg', img)       
        
        img = img.astype(np.uint8)                #change dtype to uint8 from float 64
        img=cv2.imread('Top_left.jpg',0)
        cv2.imshow('Top_left',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
        


goat=Image_compression('goat.jpg')
goat.topLeft()

