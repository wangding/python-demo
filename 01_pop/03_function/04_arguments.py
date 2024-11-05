def sumx(*args):
  return sum(args)

print(sumx(1, 2))
print(sumx(1, 2, 3))
print(sumx(1, 2, 3, 4))

def prt_kv(**args):
  for key, val in args.items():
    print(f'{key}: {val}')

prt_kv(name='zhangsan')
prt_kv(name='zhangsan', age=20)