total = int(input('Please input n[1-9]: '))
for n in range(1, total+1):
  for m in range(1, n+1):
    exp = f'{m}×{n}={m*n}'
    if m==2 and (n==3 or n==4):
      print(f'{exp:6}', end=' ')
    else:
      print(exp, end=' ')
  print('')
