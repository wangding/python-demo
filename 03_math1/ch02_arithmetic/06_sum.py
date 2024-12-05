# 循环求和

def mySum(n):
  running_sum = 0
  for i in range(n+1):
    running_sum += (i**2 + 1)
  return running_sum

print(mySum(20))