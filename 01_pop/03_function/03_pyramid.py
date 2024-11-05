import sys

def pyramid(n):
  for i in range(n+1):
    spaces = ' ' * (n - i)
    starts = '*' * (2*(i-1) + 1)
    print(spaces + starts)

def main():
  if len(sys.argv) != 2:
    print('Missing argument!')
    print('Usage: command number-of-layers')
    return
  

  num = sys.argv[1]

  if not num.isdigit():
    print(f'{num} is not a number!')
    return

  num = int(num)

  if num<1 or num>20:
    print(f'{num} is not between 1 and 20!')
    return
  
  pyramid(num)

main()