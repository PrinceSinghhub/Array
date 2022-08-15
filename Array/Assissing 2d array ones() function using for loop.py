from numpy import *
a=ones((3,2),dtype=int)
print(a)

#witout index
for r in a:
    for c in r:
        print(c)
    print()

#with index
print("with index")
n=len(a)
for i in range (n):
    for j in range (len(a[i])):
        print(a[i][j])
    print()