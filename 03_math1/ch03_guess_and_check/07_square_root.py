# 用猜测验证法求平方根
# 也叫二分查找法

def average(a, b):
  return (a + b) / 2

def square_root(num, low, high):
  for i in range(20):
    root = average(low, high)
    print('%2d   ' % i, root)
    if root ** 2 == num:
      break
    elif root ** 2 < num:
      low = root
    else:
      high = root
  return root

square_root(60, 7, 8)