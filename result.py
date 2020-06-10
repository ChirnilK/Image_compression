
import py_project
import cv
import time
import matplotlib.pyplot as plt

def time_function(f, *args):
    """This function checks how much time a function takes to run"""
    tic = time.time()
    f(*args)
    toc = time.time()
    return toc - tic

#compressing by OpenCV
cv_N=[2,4,8,16]
cv_comp=[time_function(cv.compressOpencv, 'tt.jpg', i) for i in cv_N]
print(cv_comp)

#compressing by my implementation
N=[1,2,3,4]
hwm=[time_function(py_project.multiComp, 'tt.jpg', i) for i in N]
print(hwm)


plt.plot(N, hwm, marker='o', label="My func")
plt.plot(N, cv_comp, marker='o', label="OpenCV")
plt.title('OpenCV vs my function')
plt.xlabel('number of compression (times)')
plt.ylabel('time(sec)')
plt.legend()
plt.show()

