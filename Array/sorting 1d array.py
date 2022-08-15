from numpy import *
a=array([100,500,60,800,9])
count=0
for i in range (len(a)):
    print(i)
    for j in range (1,len(a)):
        print(j)
        if a[j-1] > a[j]:
            count+=1
            a[j-1],a[j] =a[j], a[j-1]
    print(a,count)
print(a)
print(type(a))