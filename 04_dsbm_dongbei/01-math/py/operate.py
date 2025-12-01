# 标量、向量、矩阵的基本运算
# ========================

import numpy as np

# 标量乘向量
print("标量乘向量:")
a = np.array([4, 10, 6])
print("a =", a)
result = 2 * a
print("2 * a =")
print(result)
print()

# 标量乘矩阵
print("标量乘矩阵:")
b = np.array([[4, 10, 6], [-2, 4, 0], [0, 4, 5]])
print("b =")
print(b)
result = 2 * b
print("2 * b =")
print(result)
print()

# 向量加向量
print("向量加向量:")
c = np.array([4, 10, 6])
d = np.array([1, 2, 3])
print("c =", c)
print("d =", d)
result = c + d
print("c + d =")
print(result)
print()

# 矩阵加矩阵
print("矩阵加矩阵:")
e = np.array([[4, 10, 6], [-2, 4, 0], [0, 4, 5]])
f = np.array([[1, 2, 3], [3, 4, 5], [7, 8, 9]])
print("e =")
print(e)
print("f =")
print(f)
result = e + f
print("e + f =")
print(result)
print()

# 矩阵 + 行向量，广播，行向量加到矩阵的每一行
print("矩阵 + 行向量 (广播):")
print("e =")
print(e)
print("d =", d)
result = e + d
print("e + d =")
print(result)
print()

# 向量的乘法和内积
# ===============

print("向量的乘法和内积:")
g = np.array([1, 0, 3])
h = np.array([1, 2, 3])
print("g =", g)
print("h =", h)

# 向量内积
dot_product = np.dot(g, h)
print("np.dot(g, h) (内积) =")
print(dot_product)
print()

# 叉积
cross_product = np.cross(g, h)
print("np.cross(g, h) (叉积) =")
print(cross_product)
print()

# 验证叉积与原向量垂直
print("验证叉积与原向量垂直:")
print("np.dot(cross_product, g) =")
print(np.dot(cross_product, g))
print("np.dot(cross_product, h) =")
print(np.dot(cross_product, h))
print()

# 点乘，对应位相乘
print("点乘，对应位相乘:")
elementwise_product = g * h
print("g * h =")
print(elementwise_product)
print()

# 矩阵乘法
# =======

print("矩阵乘法:")
j = np.array([[1, 0, 3], [0, 2, 4]])
k = np.array([[1, 1], [2, 0], [3, 2]])
print("j =")
print(j)
print("k =")
print(k)
matrix_product = np.dot(j, k)
print("np.dot(j, k) =")
print(matrix_product)
print()

# 矩阵乘法应用
# ===========

print("矩阵乘法应用:")
# 产品a 和 产品b 的三项成本构成
l = np.array([[1, 1], [2, 3], [3, 5]])
# 产品a 和 产品b 四个季度的产量
m = np.array([[100, 150, 180, 120], [300, 200, 240, 180]])
print("成本构成矩阵 l =")
print(l)
print("产量矩阵 m =")
print(m)

# 计算每个成本项在每个季度的总成本
quarterly_costs = np.dot(l, m)
print("季度成本矩阵 (l * m) =")
print(quarterly_costs)

# 求总成本
total_cost = np.sum(quarterly_costs)
print("总成本 (sum(l * m)) =")
print(total_cost)
print()

# 矩阵除法和逆矩阵
# ===============

print("矩阵除法和逆矩阵:")
n = np.array([[2, 3], [4, 5]])
print("n =")
print(n)
o = np.linalg.inv(n)
print("np.linalg.inv(n) (逆矩阵) =")
print(o)

# 验证逆矩阵
identity = np.dot(n, o)
print("n * o (应为单位矩阵) =")
print(identity)
print()

# 矩阵除法（左除和右除）
print("矩阵除法:")
# 左除: a / b = a * inv(b)
# 右除: a \ b = inv(a) * b
print("注意: 在NumPy中，左除使用 np.divide(a, b) 或 a / b (对应元素除法)")
print("      矩阵左除 (a * inv(b)) 使用 np.dot(a, np.linalg.inv(b))")
print("      矩阵右除 (inv(a) * b) 使用 np.linalg.solve(a, b) 或 np.dot(np.linalg.inv(a), b)")
print()

# 矩阵转置
# =======

print("矩阵转置:")
print("k =")
print(k)
k_t = k.T
print("k.T (转置) =")
print(k_t)