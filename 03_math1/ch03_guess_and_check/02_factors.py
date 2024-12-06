# 求整数的因数列表

def factors(num):
  factors_list = []
  for factor in range(1, num+1):
    if(num % factor == 0):
      factors_list.append(factor)
  return factors_list

print(factors(120))