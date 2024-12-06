# 用猜测验证法求方程的根

def average(a, b):
  return (a + b) / 2

def f(x):
  return 6*x**3 + 31*x**2 + 3*x - 10

def guess(low, high):
  for i in range(20):
    root = average(low, high)
    # print('%2d   ' % i, root)
    if f(root) == 0:
      break
    elif f(root) > 0:
      low = root
    else:
      high = root
  return root

print(guess(-1, 0))
print(guess(0, 1))
