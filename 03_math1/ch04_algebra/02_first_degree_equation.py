# 解一元一次方程
# ax + b = cx + d
# x = (d-b) / (a-c)

def equation(a, b, c, d):
  return (d-b) / (a-c)

print(equation(2, 5, 0, 13))
print(equation(12, 18, -34, 67))
print(equation(1/2, 2/3, 1/5, 7/8))