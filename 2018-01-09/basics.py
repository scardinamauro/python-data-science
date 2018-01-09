# 1 - lists
# order is important - mutable

odds = [5,7,9]

total = 0
for num in odds:
    total = total + num
    #total += num

total = 0
for i,num in enumerate(odds): # enumerate returns a TUPLE
    total = total + (i * num)

# List comprehension - use instead of for loops
cube = [n**2 for n in odds]
squareroots = [n**0.5 for n in odds]
cuberoots = [n**0.33 for n in odds]
divisableby5 =  [ n for n in range(31) if n%5==0]

# In line functions use map and lambda
list(map(lambda n: n**(1/3), odds))

# Use filter instead of map to select certain values from a list
list(filter(lambda n: n <= 7, odds))

# Use reduce to perform an operation on a list and return a single value
from functools import reduce
reduce(lambda total, n: total * n, odds, 1)

# 2 - Tuple
# Ordered but immutable
tup1 = (3,4)

# 3 - sets
# no order, iterable, unique values, mutable, only takes immutable/hashable values
set = {5,3,7,8}

s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8}

s1 & s2
# Out[36]: {5, 6}

s1 | s2
# Out[37]: {1, 2, 3, 4, 5, 6, 7, 8}

s1 ^ s2
# Out[38]: {1, 2, 3, 4, 7, 8}

# 4 - Dictionaries
# no order, iterable, unique keys (only), keys hashable/imutable (only)
d = {}
for n in range(5):
    d[n] = n**2
d.get(5, 'default')

{n: n**0.5 for n in range(50) if n % 10 == 0}
[(n, n**0.5) for n in range(50) if n % 10 == 0]

d.get(n) # Returns the value of the dictionary at the nth key - if a v
d.get(5, 'default')

# Dictionary comprehension
{ n:n**0.5 for n in range(100) if n%10==0}
Out[58]:
{0: 0.0,
 10: 3.1622776601683795,
 20: 4.47213595499958,
 30: 5.477225575051661,
 40: 6.324555320336759,
 50: 7.0710678118654755,
 60: 7.745966692414834,
 70: 8.366600265340756,
 80: 8.94427190999916,
 90: 9.486832980505138}

 [(n,n**0.5) for n in range(50) if n%10==0]
Out[60]:
[(0, 0.0),
 (10, 3.1622776601683795),
 (20, 4.47213595499958),
 (30, 5.477225575051661),
 (40, 6.324555320336759)]
