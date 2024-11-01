import math
import sys

def h(p):
  if p == 0 or p == 1:
    return 0

  return -p * math.log2(p) - (1-p) * math.log2(1-p)

def validate(p):
  if not type(p) in [int, float]:
    print(f'Probability {p} is not a number!')
    return False

  if p<0 or p>1:
    print(f'Probability {p} is not between 0 and 1!')
    return False

  return True

def main():
  if len(sys.argv) != 2:
    print('Missing probability!');
    print('Usage: command probability');
    return

  p = float(sys.argv[1])

  if not validate(p):
    return

  print(f'h({p}) = {h(p):.3f} bit')

main()