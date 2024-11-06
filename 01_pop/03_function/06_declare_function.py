# 声明方式 1，def 关键字
def sayHello_1(name):
  print(f'Hello, {name}.')

sayHello_1('wangding')

# 声明方式 2，函数表达式
sayHello_2 = lambda name: print(f'Hello, {name}.')

sayHello_2('wangding')

# 函数名是 function 类型的变量
print(type(sayHello_1))

# 函数是对象，就有属性
print(sayHello_1.__name__)
print(sayHello_2.__code__)
print(sayHello_1.__module__)

# 函数是对象，就有方法
print(sayHello_1.__dir__())
print(sayHello_1.__str__())