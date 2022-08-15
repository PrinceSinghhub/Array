from numpy import *
#a=array([1,2,3,4,5]) show error becouse len are not same
a=array([[1,2,3],[4,5,6]])
b=reshape(a,(9))
# c=reshape(a,(5)) SHOW erreo becouse we have to 6 element bur put 5 combination are not matched
print(b)
# print(c)