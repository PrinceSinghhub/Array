import numpy

# First methode
a = numpy.array([1, 2, 3, 4, 5])
print(a)
print(type(a))
b = numpy.array([1.3, 2.0, 3.8, 4.9, 5.6])
print(b)
print(type(b))
c = numpy.array(['prince', 'khushi', 'king', 'future'])
print(c)
print(type(c))

from numpy import *

a = array([1, 2, 3, 4, 5])
print(a)
print(type(a))
b = array([1.3, 2.0, 3.8, 4.9, 5.6])
print(b)
print(type(b))
c = array(['prince', 'khushi', 'king', 'future'])
print(c)
print(c.dtype)
print(type(c))

# indexing
from numpy import *

a = array([1, 2, 3, 4, 5])
b = len(a)
for i in range(b):
    print(a[i])

# Acessing 1D Array
from numpy import *

a = array([1, 2, 3, 4, 5])
print(a[0], a[1], a[2], a[3], a[4])

# Modifying 1D array
from numpy import *

a = array([1, 2, 3, 4, 5])
a[2] = 6
print(a.dtype)
print(a)

# Acessing 1D Array by loop
from numpy import *

# without index
a = array([1, 2, 3, 4, 5])
for i in a:
    print(i)

# with index
a = array([1, 2, 3, 4, 5])
b = len(a)
for i in range(b):
    print(a[i])

# while loop 1D Array
a = array([1, 2, 3, 4, 5])
b = len(a)
i = 0
while i < b:
    print(a[i])
    i += 1

# Creating 1D array using linespace () Function
from numpy import *

a = linspace(1, 8, endpoint=True)
print(a)
a = linspace(1, 8, endpoint=False)
print(a)

a = linspace(1, 8, 5, endpoint=True)
print(a)
a = linspace(1, 8, 5, endpoint=False)
print(a)

# Acessingh array
a = linspace(1, 8, 5)
# without index
for i in a:
    print(i)

# with index
a = linspace(1, 8, 5)
b = len(a)
for i in range(b):
    print(a[i])

# Accessing with while loop
a = linspace(1, 8, 5)
b = len(a)
c = 0
while c < b:
    print(a[c])
    c += 1

# Ceating array using logspace
from numpy import *

a = logspace(1, 3, 5, base=2)
print(a)

a = logspace(1, 3, 5, base=2, endpoint=False)
print(a)

# Accersingh element
# without index
a = logspace(1, 3, 5, base=3)
for i in a:
    print(i)

# with index
a = logspace(1, 3, 5, base=3)
b = len(a)
for i in range(b):
    print(a[i])

# AcceSsingh bi while loop
a = logspace(1, 3, 5, base=3)
b = len(a)
c = 0
while c < b:
    print(a[c])
    c += 1

# Creating 1D array by using arange() Function
from numpy import *

n = arange(5)
print(n)

n = arange(1, 6)
print(n)

n = arange(1, 6, 2)
print(n)

# accesing 1d array
# without index
n = arange(1, 6, 2)
for i in n:
    print(i)

# with index
n = arange(1, 6, 2)
b = len(n)
for i in range(b):
    print(n[i])

# accessing array using while loop
a = arange(1, 6, 2)
b = len(a)
c = 0
while c < b:
    print(a[c])
    c += 1

# 1D array using zero() function
from numpy import *

a = zeros(5)
print(a)

a = zeros(5, dtype=int)
print(a)

# assing array
# without index
a = zeros(5, dtype=int)
for i in a:
    print(i)

# with index
a = zeros(5, dtype=int)
b = len(a)
for i in range(b):
    print(a[i])

# assising by while loop
a = zeros(5, dtype=int)
b = len(a)
c = 0
while c < b:
    print(a[c])
    c += 1

# 1D array using once() function

from numpy import *

a = ones(5, dtype=int, order='C')
print(a)

# without index
a = ones(5, dtype=int, order='C')
for i in a:
    print(i)

# with index
a = ones(5, dtype=float, order='C')
b = len(a)
for i in range(b):
    print(a[i])

# assising by while loop
a = ones(5, dtype=float, order='C')
b = len(a)
c = 0
while b > c:
    print(a[c])
    c += 1

















































