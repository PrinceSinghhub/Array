from numpy import *
a=array([100,200,300,400,500])
b=nonzero(a)
print(b)

#now put zero value
a=array([100,200,0,300,400,0,500,0])
b=nonzero(a)
print(b)

a=array([0,100,200,0,300,400])
b=nonzero(a)
print(b)