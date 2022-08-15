from numpy import *
n=int(input("Enter your row = "))
m=int(input("Enter your collom = "))
x=zeros((n,m),dtype=int)
# before assingne vale in array
print(x)
y=len(x)
# after the assigine the value
for i in range(y):
    for j in range(len(x[i])):
        z=n=int(input("Enter the element = "))
        x[i][j]=z
        #show the all process of accessesing element in array
        # print(x)
#only show our finally array
print(x)

# asscessign the element of array
for i in range(y):
    for j in range(len(x[i])):
        print("index of",i,j,"=",x[i][j])
