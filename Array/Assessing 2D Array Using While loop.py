from numpy import *
a=array([[1,2,3,4,5],[6,7,8,9,10]])
n=len(a)
print(n)
print(a[0])
print(a[1])
i=0
while i<n:
    j=0
    while j <len(a[i]):
        print('index',i,j,'=',a[i][j])
        j+=1
    i+=1
