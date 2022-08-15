from numpy import *
#a=array([1,2,3,4,5]) show error becouse len are not same
a=array([1,2,3,4,5,6])
b=reshape(a,(2,3))
c=reshape(a,(3,2))
print(b)
print(c)