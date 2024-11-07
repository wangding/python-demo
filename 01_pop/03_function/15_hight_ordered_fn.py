arr = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, arr))
print(squared)

odd = list(filter(lambda x: x%2, arr))
print(odd)

from functools import reduce

total = reduce(lambda x, y: x + y, arr)
print(total)