total = int(input('Please input n[1-9]: '))
for n in range(1, total+1):
  for m in range(1, n+1):
    if m==2 and (n==3 or n==4):
      print(f'{m}×{n}={m*n:<2}', end=' ')
    else:
      print(f'{m}×{n}={m*n}', end=' ')
  print('')
