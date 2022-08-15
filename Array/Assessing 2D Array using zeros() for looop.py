from numpy import *
a=zeros((3,2),dtype=int)

#without index
for r in a:
    for c in r:
        print(c)
    print()

#with index
print("With index")
n=len(a)
for i in range (n):
    for j in range (len(a[i])):
        print(a[i][j])
    print()