# 蛮力法，代入数据解一元一次方程

def plug():
  x = -100
  while x < 100:
    if 2*x + 5 == 13:
      print('x = ', x)
      break
    x += 1
    print(x)

plug()