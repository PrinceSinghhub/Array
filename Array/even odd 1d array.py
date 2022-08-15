from numpy import * #'numpy.ndarray' object has no attribute 'append'
from array import *
a=array('i',[])
n=int(input("enter a range of array"))
for i in range (n):
    n2=int(input("Enter a Value of Array"))
    a.append(n2)
print(a)
print(type(a))
val = len(a)
print("lenth of array is",val)
old=array('i',[])
ev=array('i',[])
for j in range (val):
    print(j)
    if a[j]%2==0:
        ev.append(a[j])
print("the even array is", ev)
for k in range (val):
    print(k)
    if a[k]%2!=0:
        old.append(a[k])
print("the old array is", old)



