from second_class import SecondClass

class ThirdClass(SecondClass):  # Inherit from SecondClass
  def __init__(self, value):  # On "ThirdClass(value)"
    self.data = value

  def __add__(self, other):  # + 运算符重载, On "self + other"
    return ThirdClass(self.data + other)  # 返回新的对象
  
  def __str__(self):  # print 运算符重载, # On "print(self)", "str()"
    # 不重载则打印 <__main__.ThirdClass object at 0x000002D8E7216900>
    # 把重载代码注释掉，运行程序就能看到效果
    return '[ThirdClass: %s]' % self.data

  def mul(self, other):  # 没有运算符重载, In-place change: named
    self.data *= other

if __name__ == '__main__':
  a = ThirdClass('abc')  # __init__ called
  a.display()  # Inherited method called
  print(a, '\n')  # __str__: returns display string

  b = a + 'xyz'   # __add__: makes a new instance
  b.display()  # b has all ThirdClass methods
  print(b, '\n')  # __str__: returns display string

  a.mul(3)  # mul: changes instance in place
  print(a, '\n')

  print(a.__dict__)
  print(a.__class__)
  print(ThirdClass.__mro__)