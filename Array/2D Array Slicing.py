from numpy import *
a=array([[10,20,30],
         [40,50,60],
        [70,80,90]])
print(a)
# slicing 0th row and oth collom
b=a[0,:]
print(b)

# another slicing
z=a[0:3:1,1:3:1]
print(z)

# if we want to print full row 0th colom
s=a[:,0]
print(s)

# if we want to print full row 2nd colom
o=a[:,1]
print(o)

# if we want to print full row 3nd colom
h=a[:,2]
print(h)

# if we want to print a particular element
i=a[0:1,0:1]
print(i)

# if we want to print a particular element 50
k=a[1:2,1:2]
print(k)

# if we want to print a particular element 90
p=a[2:,2]
print(p)

# also write 90
p=a[2:3,2:3]
print(p)

# if we want to print a particular element between range
l=a[0:2,1:3]
print(l)