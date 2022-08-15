from numpy import *
a=array([[1,2,3,4,5],[6,7,8,9,10]],dtype=float)
a[0][2]=300
a[1][3]=900
print(a)
print(a.dtype)