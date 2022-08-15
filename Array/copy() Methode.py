from numpy import *
a=array([1,2,3,4,5])
b=copy(a)
print(a)
print(b)

#now change the some vallue of array a
a[1]=700
print(a)
print(b)

#now change the some vallue of array b
b[2]=900
print(a)
print(b)
