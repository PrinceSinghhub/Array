#1st methode
import array
n=array.array('i',[1,2,3,4,5])
print(n[0])
for i in range(len(n)):
    print(n[i])
#2nd methhode
from array import *
n=array('i',[1,2,3,4,5])
print(n[3])
for i in range(len(n)):
    print(n[i])