from numpy import *
n=int(input("Enter your row = "))
m=int(input("Enter your collom = "))
x=zeros((n,m),dtype=int)
# before assingne vale in array
print(x)
y=len(x)
# after the assigine the value
i=0
while(i<y):
    j=0
    while(j<len(x[i])):
        z = n = int(input("Enter the element = "))
        x[i][j]=z
        j+=1
    i+=1
print(x)

# element accessing
a=0
while(a<y):
    t=0
    while(t<len(x[a])):
        print('index of',a,t,'=',x[a][t])
        t+=1
    a+=1


