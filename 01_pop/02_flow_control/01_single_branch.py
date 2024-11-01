import sys

age = int(input('请输入你的年龄：'))

if age > 25 or age < 15:
  print(f'{age} 岁不是合法的本科入学年龄' )
  sys.exit()

print(f'{age} 岁适合在大学里读书深造')