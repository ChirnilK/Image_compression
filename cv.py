
import cv2
import sys

"""This is the code using built-in function of OpenCV to compress a grayscale image.
   I commented out some codes for measuring the execution time."""

def compressOpencv(filename, n=2):
    """This function requires two imputs, filename and n. 
       n is the number that you want to devide the height and the width of the image.
       If the file path doesn't exist, then the system will close."""
    
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