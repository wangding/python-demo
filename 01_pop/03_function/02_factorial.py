import sys

def factorial_recursion(n):
  return 1 if n == 1 else n * factorial_recursion(n - 1)

def factorial_loop(n):
  fact = 1
  for i in range(1,n+1):
    fact *= i
  return fact

def main():
  if len(sys.argv) != 2:
    print('Missing argument!')
    print('Usage: command number')
    return

  num = sys.argv[1]
  
  if not num.isdigit():
    print(f'{num} is not a integer number!')
    return
  
  num = int(num)

  if num < 0 or num > 20:
    print(f'{num} is out of rang (0, 20)!')
    return 

  print(f'loop:      {num}! = {factorial_loop(num)}')
  print(f'recursion: {num}! = {factorial_recursion(num)}')

main()