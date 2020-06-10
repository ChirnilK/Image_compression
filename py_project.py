
import numpy as np
import cv2
import sys

"""This is my function for compressing an grayscale image with Haar Wavelets.
   I commented out some codes for measuring the execution time. """

def readImg(filename):
    """ The function requires one input, filename with the format. A color image or 
        a format other than jpg can be taken in however it will be transformed into 
        a grayscale image and saved as a jpg file.
        If the file path doesn't exist, then the system will close. """
        
    img = cv2.imread(filename)

    if img is None:
        print("Failed to load image file.")
        sys.exit(1)
        
    imgArray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #height, width = imgArray.shape
    #print('Original image size is {}x{}'.format(height, width))
        
    # cv2.imshow('Original Gray Image',imgArray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()  
    
    return compression(imgArray)
   


def trim(img):
    """This function makes sure that the image have an even number of pixels, else the haar-transform will not work.
       If the rows/columns of the image is odd then cut off the last row/column and save the image.
       The function will return an image that has been trimmed and/or saved as an array and 
       its height and width"""
    
    height, width = img.shape
    
    if height % 2 !=0:
        img = img[:-1]
        #print ('Image was uneven (width-wise) and has been trimmed!')

    if width %2 !=0:
        imgT = img.transpose()
        imgT = imgT[:-1]
        img = imgT.transpose()
        #print ('Image was uneven (height-wise) and has been trimmed!')

    height, width = img.shape
    #print('Trimmed image size is {}x{}'.format(height, width))

    # cv2.imwrite('Trimmed_img.jpg', img)
    # img=cv2.imread('Trimmed_img.jpg',0)
        
    return img, height, width
    


def haar(sz):
    """This function creates the Haar-matrix. The input is the size of require Haar array.
       The return is a Haar array."""

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


def compression(imgArray):
    """This function trims and compresses an image using dot-products and the Haar-matrix"""
    img, m_size, n_size = trim(imgArray)
    w_m=haar(m_size)
    w_t=haar(n_size).T

    comp=np.dot(np.dot(w_m,img),w_t)
    # cv2.imwrite('Compressed_img.jpg', comp) 
    # comp = comp.astype(np.uint8)       #change dtype to uint8 from float 64
    # comp=cv2.imread('Compressed_img.jpg',0)
    # cv2.imshow('Compressed_img.jpg',comp)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()  
    
    return comp   

def topLeft(comp_img):
    """This function cuts the top-left fourth of the image"""
    imgz = comp_img.shape
    img = np.array(comp_img[0:imgz[0]//2, 0:imgz[1]//2])
    # cv2.imwrite('Top_left.jpg', img)       
    
    # img = img.astype(np.uint8) #change dtype to uint8 from float 64
    # img=cv2.imread('Top_left.jpg',0)
    # height, width = img.shape
    # print('Compressed and cut image size is {}x{}'.format(height, width))
    # cv2.imshow('Top_left.jpg',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()  
    
    return img

def multiComp(filename, times):
    """This function compresses a image as many times as the you tell it to.
       It requires two inputs, filename and times. times is how many compressions you want to do.
       You will get an error message when the result will be too small."""
   
    compd = readImg(filename)
    min_size=min(compd.shape[0], compd.shape[1])
    
    if min_size//(2*times)<100:
        print('The image is too small to be compressed {} times.'.format(str(times)))
        sys.exit(1)
        
    else:
        if times == 1:
            return topLeft(compd)
        else:    
            while times > 1:
                compd = topLeft(compd)
                compd = compression(compd)
                times -= 1
                   
    return topLeft(compd)
        
multiComp('tt.jpg', 1)