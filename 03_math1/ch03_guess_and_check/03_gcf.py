# 求两个整数的最大公因数
# greatest common factor，GCF

def factors(num):
  factors_list = []
  for factor in range(1, num+1):
    if(num % factor == 0):
      factors_list.append(factor)
  return factors_list

def gcf(fcts_a, fcts_b):
  fcts_a.reverse()
  fcts_b.reverse()

  if len(fcts_a) < len(fcts_b):
    fcts_short = fcts_a
    fcts_long  = fcts_b
  else:
    fcts_short = fcts_b
    fcts_long  = fcts_a
  
  for factor in fcts_short:
    if factor in fcts_long:
      return factor

print(factors(6))
print(factors(7))
print(gcf(factors(6), factors(7)))