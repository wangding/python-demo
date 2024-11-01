import sys

n = int(input('请输入整数 n[1-50]: '))

if n<1 or n>50:
  print(f'{n} 超出了取值范围 [1-50]')
  sys.exit()

fact = 1
for i in range(1, n+1):
  fact *= i

print(f'{n}! = {fact}')