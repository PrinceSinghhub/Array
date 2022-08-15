from array import*
#insert in array
b=array('i',[1,2,3,4,5])
b.insert(4,20)
print(b)

#pop in array
a=array('i',[1,2,3,4,5])
a.pop(2)
b=array('i',[1,2,3,4,5])
b.pop()
print(b)

#remove in array
a=array('i',[1,2,3,4,5])
a.remove(2)
print(a)

#index in array
a=array('i',[1,2,3,4,5])
n=a.index(5)
print(n)

#reverse in array
a=array('i',[1,2,3,4,5])
a.reverse()
print(a)

#extend in array
a=array('i',[1,2,3,4,5])
b=array('i',[6,7,8,9,10])
a.extend(b)
print(a)

#slicing on array
a=array('i',[1,2,3,4,5])
print(a)
n=len(a)
print(n)
for i in range (n):
    print(i,a[i])
#slicing
z=a[1:5]
print(z )
for i in z:
    print(i)

#negative slicing
a=array('i',[1,2,3,4,5,6,7])
n=a[-5:-3]
print(n)

#stepindex
a=array('i',[1,2,3,4,5,6,7,8,9,10])
z=a[0:11:2]
print(z)
for i in a[0:11:2]:
    print(i)



















