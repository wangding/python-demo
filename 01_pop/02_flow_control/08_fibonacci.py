import sys

n = int(input('请输入数量 n[5-20]: '))

if n<5 or n>20:
    print(f'{n} 超出范围 [5-20]')
    sys.exit()

i = 2
fibonacci = [0, 1];

while i <= n:
  fibonacci.append(fibonacci[i-1] + fibonacci[i-2]);
  i += 1

print(fibonacci)