from numpy import *
a=zeros((3,2),dtype=int)
n=len(a)
i=0
while i<n:
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1