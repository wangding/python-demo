import sys

def factorial(n):
  return 1 if n == 1 else n * factorial(n - 1)

def validate():
  if len(sys.argv) != 2:
    print('Missing argument!')
    print('Usage: command number')
    return None

  num = sys.argv[1]
  
  if not num.isdigit():
    print(f'{num} is not a integer number!')
    return None
  
  num = int(num)

  if num < 0 or num > 20:
    print(f'{num} is out of rang (0, 20)!')
    return None
  
  return num
  
def main():
  num = validate()
  if num != None:
    print(f'{num}! = {factorial(num)}')

main()