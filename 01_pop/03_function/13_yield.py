def count_up_to(n):
  for i in range(1, n + 1):
    yield i * 2

for number in count_up_to(5):
  print(number)