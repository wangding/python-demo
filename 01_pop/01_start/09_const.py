# 方式一、使用大写字母命名约定
PI = 3.14159
GRAVITY = 9.81

print('method_1:')
print(PI)
print(GRAVITY)

PI = 4.3
print(PI)

# 方式二、使用 enum 模块
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print('\nmethod_2:')
print(Color.RED)
print(Color.RED.value)

# 方式三、使用 types 模块的 MappingProxyType
from types import MappingProxyType

constants = MappingProxyType({
    'PI': 3.14159,
    'GRAVITY': 9.81
})

print('\nmethod_3:')
print(constants['PI'])
print(constants['GRAVITY'])

# 尝试修改常量会抛出 TypeError
# constants['PI'] = 4.31  # 抛出 TypeError: 'mappingproxy' object does not support item assignment

# 方式四、使用类来封装常量，只读属性
class Constants:
    def __init__(self):
        self._pi = 3.14159
        self._gravity = 9.81

    @property
    def pi(self):
        return self._pi

    @property
    def gravity(self):
        return self._gravity

constants = Constants()

print('\nmethod_4:')
print(constants.pi)
print(constants.gravity)

# 尝试修改常量会抛出 AttributeError
# constants.pi = 4.31  # 抛出 AttributeError: can't set attribute