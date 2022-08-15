from array import *
n = array('i', [])
n1 = int(input("Enter a Range"))
for i in range(n1):
    n2 = int(input("Enter a Value"))
    n.append(n2)
for j in range(len(n)):
    print(n[j])
print(type(n))