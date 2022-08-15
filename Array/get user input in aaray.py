from numpy import *
n=int(input("Enter a rnage of array"))
a=zeros(n,dtype=int)
print(a)

#now the change the value of zerro array
b=len(a)
for i in range (b):
    x = int(input("Enter a value"))
    a[i]=x
print(a)