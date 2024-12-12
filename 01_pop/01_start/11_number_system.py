num10 = 34

# 十进制转二、八、十六进制
num2  = bin(num10)
num8  = oct(num10)
num16 = hex(num10)

print(f'{num10} => {num2}')
print(f'{num10} => {num8}')
print(f'{num10} => {num16}')
print()

# 二、八、十六进制转十进制
print(f'{num2} => {int(num2, 2)}')
print(f'{num8} => {int(num8, 8)}')
print(f'{num16} => {int(num16, 16)}')
print()

# 二、八、十六进制的 11 的十进制是多少
print(f'0b11 => {int("0b11", 2)}')
print(f'0o11 => {int("0o11", 8)}')
print(f'0x11 => {int("0x11", 16)}')