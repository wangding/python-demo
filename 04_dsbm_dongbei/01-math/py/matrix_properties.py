import numpy as np

# 函数，函数是映射
# =============

# 函数的参数可以是标量
x = 4
y = np.sqrt(x)
z = np.sin(y)
print("标量操作:")
print(f"x = {x}")
print(f"y = sqrt(x) = {y}")
print(f"z = sin(y) = {z}")
print()

# 函数的参数可以是向量
a = np.array([4, 5, 6])
b = np.array([1, 2, 3])
c = np.dot(a, b)  # 向量点积
print("向量操作:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = dot(a, b) = {c}")
print()

# 函数的参数可以是矩阵
d = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])
diag_d = np.diag(d)  # 主对角线
print("矩阵操作:")
print(f"d = \n{d}")
print(f"diag(d) = {diag_d}")
print()

# 向量范数
# =======

v = np.array([2, 3, -5, -7])
print("向量范数:")
print(f"v = {v}")

# 1范数：向量各元素绝对值之和
norm_1 = np.linalg.norm(v, 1)
print(f"1范数: ||v||₁ = {norm_1}")

# 2范数：欧几里得范数（向量模长）
norm_2 = np.linalg.norm(v, 2)
print(f"2范数: ||v||₂ = {norm_2}")

# p范数（以p=3为例）
p = 3
norm_p = np.linalg.norm(v, p)
print(f"{p}范数: ||v||ₚ = {norm_p}")

# 正无穷范数：向量元素绝对值的最大值
norm_inf = np.linalg.norm(v, np.inf)
print(f"正无穷范数: ||v||_∞ = {norm_inf}")

# 负无穷范数：向量元素绝对值的最小值
norm_neg_inf = np.linalg.norm(v, -np.inf)
print(f"负无穷范数: ||v||_{-np.inf} = {norm_neg_inf}")
print()

# 矩阵范数
# =======

e = np.array([[-1, 0, 5], [2, 4, 6], [0, 4, 5]])
print("矩阵范数:")
print(f"e = \n{e}")

# 矩阵1范数（列和范数）
mat_norm_1 = np.linalg.norm(e, 1)
print(f"矩阵1范数: ||e||₁ = {mat_norm_1}")

# 矩阵2范数（谱范数）
mat_norm_2 = np.linalg.norm(e, 2)
print(f"矩阵2范数: ||e||₂ = {mat_norm_2}")

# 矩阵无穷范数（行和范数）
mat_norm_inf = np.linalg.norm(e, np.inf)
print(f"矩阵无穷范数: ||e||_∞ = {mat_norm_inf}")
print()

# 矩阵的秩
rank_d = np.linalg.matrix_rank(d)
print(f"矩阵d的秩: rank(d) = {rank_d}")
print()

# 特征值和特征向量
f = np.array([[2, 1, 0], [1, 3, 1], [0, 1, 4]])
print("特征值和特征向量:")
print(f"f = \n{f}")

# 计算特征值和特征向量
# 注意：NumPy返回的特征向量是归一化的
vals, vecs = np.linalg.eig(f)
print("特征值:")
print(vals)
print("特征向量（按列排列）:")
print(vecs)