# Image_compression with Haar Wavelets

This is my school project on image compression with Haar Wavelets.

I study a method for compressing a grayscale image. 
The mathematical method is called Haar wavelets - a method based on simply taking arithmetic means and differences.
The theory is explained in this link :
http://www.whydomath.org/node/wavlets/hwt.html

The result will be saved as a jpg-file but you can compress png-file as well.



### class_comp.py

The code is written as a class/object style.
Here you can compress a picture one time which means the picture size will be 1/4 (n/2 x m/2) when original size is (m x n).



### Multi comp.ipynb (Jupyter Notebook)

In here, you can see the output one piece at a time.
Now you can compresses a image as many times as the you tell it to.(The size is limited)


### result.py / cv.py / py_project.py

When you run the file, result.py, you will see how long each function (OpenCV, reshape, and my function for compressing an image) takes time for 1, 2, 3, 4 compressions. Clearly, reshape function of OpenCV is much faster than my function.




