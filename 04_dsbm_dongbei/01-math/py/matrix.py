import numpy as np

# 2X3 矩阵
a = np.array([[1, 2, 3], [4, 5, 6]])
print("2X3矩阵:")
print(a)

# 取第1行
b = a[0, :]  # Python是0索引，所以第一行是索引0
print("第1行:", b)

# 取第2列
c = a[:, 1]  # 第二列是索引1
print("第2列:", c)

# 取1行3列
d = a[0, 2]  # 第一行第三列是索引(0,2)
print("第1行第3列的元素:", d)

# 3X3 的方阵
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("3X3方阵:")
print(a)

# 取下三角
b = np.tril(a)
print("下三角矩阵:")
print(b)

# 取上三角
c = np.triu(a)
print("上三角矩阵:")
print(c)

# 取主对角线
d = np.diag(a)
print("主对角线元素:", d)

# nxm 的单位矩阵
a = np.eye(3, 4)
print("3X4单位矩阵:")
print(a)

# nxm 的全 1 矩阵
b = np.ones((3, 4))  # numpy中参数需要是元组
print("3X4全1矩阵:")
print(b)

# nxm 的全 0 矩阵
c = np.zeros((3, 4))
print("3X4全0矩阵:")
print(c)

# nxm 的随机矩阵
d = np.random.rand(3, 4)  # 生成[0,1)之间的随机数
print("3X4随机矩阵:")
print(d)