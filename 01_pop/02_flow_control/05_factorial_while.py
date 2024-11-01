import sys

n = int(input('请输入整数 n[1-50]: '))

if n<1 or n>50:
  print(f'{n} 超出了取值范围 [1-50]')
  sys.exit()

fact, i = 1, 1
while i <= n:
  fact *= i
  i += 1

print(f'{n}! = {fact}')