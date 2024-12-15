x1 = [{0}] * 3
print('x1 id:', id(x1))
for i in range(3):
  print(f'x1[{i}] id:', id(x1[i]), x1[i])
x1[0].add(1)
for i in range(3):
  print(f'x1[{i}] id:', id(x1[i]), x1[i])

x1 = [{1}, {2}, {3}]
print('\nx1 id:', id(x1))
for i in range(3):
  print(f'x1[{i}] id:', id(x1[i]), x1[i])

x2 = x1
print('\nx2 id:', id(x2))
for i in range(3):
  print(f'x2[{i}] id:', id(x2[i]), x2[i])

# 浅拷贝
x3 = list(x1)
print('\nx3 id:', id(x3))
for i in range(3):
  print(f'x3[{i}] id:', id(x3[i]), x3[i])

# 深拷贝
import copy
x4 = copy.deepcopy(x1)
print('\nx4 id:', id(x4))
for i in range(3):
  print(f'x4[{i}] id:', id(x4[i]), x4[i])