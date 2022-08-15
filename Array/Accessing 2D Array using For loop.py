from numpy import *
a=array([[1,2,3,4,5],[6,7,8,9,10]])
#without index
for r in a:
    print(r)
    for c in r:
        print(c)
    print()

#with index

from numpy import *
a=array([[1,2,3,4,5],[6,7,8,9,10]])
n=len(a)
print(n)
print(a[0])
print(a[1])
print(len(a[0]))
for i in range (n):
    for j in range (len(a[i])):
        print(a[i][j])
    print()