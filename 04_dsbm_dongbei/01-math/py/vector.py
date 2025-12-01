import numpy as np

# 行向量
a = np.array([1, 2, 3, 4, 5])
print("行向量:", a)

# 列向量
b = np.array([[1], [2], [3], [4], [5]])
print("列向量:")
print(b)

# 向量转置
c = b.T  # 对于numpy数组，转置使用.T属性
print("列向量转置为行向量:", c)

# 冒号生成向量 (类似于MATLAB的 1:5)
d = np.arange(1, 6)  # numpy的arange是左闭右开区间
print("生成1到5的向量:", d)

# 冒号指定步长 (类似于MATLAB的 1:2:10)
e = np.arange(1, 11, 2)
print("生成1到10步长为2的向量:", e)

# 函数生成向量，默认生成50个元素 (MATLAB默认是100个)
f = np.linspace(1, 10)  # numpy默认生成50个点
print("linspace生成1到10的向量(默认50个点):", f)
print("向量长度:", len(f))

# 指定数量
g = np.linspace(1, 10, 5)
print("linspace生成1到10的向量(指定5个点):", g)

# 对数等分
h = np.logspace(1, 5, 3)
print("logspace生成10^1到10^5的对数等分(3个点):", h)