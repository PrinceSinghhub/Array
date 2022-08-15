from numpy import *
a=array([101,102,103,104,105])
b=array([101,2,3,4,5])
c=where(a>b,a,b)
d=where(a<b,a,b)
print(c)
print(d)