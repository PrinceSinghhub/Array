from numpy import *
n=int(input("Range"))
a=zeros(n,dtype=int)
print(a)

#now the change the value of zerro array
b=len(a)
c=0
d=0
while c<b:
    n = int(input("value"))
    a[c]=n
    c+=1
print(a)

while d<b:
    print(a[d])
    d+=1

