from numpy import*
a=array([100,200,300,400,500])
b=a.view()
print(a)
print(b)
print(id(a))
print(id(b))
#now change the some vallue of array a
a[1]=700
b[2]=900
print(a)
print(b)
print(id(a))
print(id(b))