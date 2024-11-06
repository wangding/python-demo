sum = lambda x, y: x + y

x = 2
y = 3
print(f'{x} + {y} = {sum(x, y)}')

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print(squared)