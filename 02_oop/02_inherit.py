import math

class Shape:
  @property
  def area(self):
    pass

  @property
  def perimeter(self):
    pass

class Circle(Shape):
  def __init__(self, radius):
    self.__r = radius

  @property
  def area(self):
    return math.pi * self.__r ** 2

  @property
  def perimeter(self):
    return 2 * math.pi * self.__r

class Triangle(Shape):
  def __init__(self, base, height):
    self.__b = base
    self.__h = height

  @property
  def area(self):
    return self.__b * self.__h / 2
  
  @staticmethod
  def perimeter(s1, s2, s3):
    return s1+s2+s3

class Rectangle(Shape):
  def __init__(self, width, height):
    self.__w = width
    self.__h = height
  
  @property
  def area(self):
    return self.__w * self.__h
  
  @property
  def perimeter(self):
    return 2 * self.__w + 2 * self.__h

class App:
  @staticmethod
  def main():
    r = Rectangle(20, 10)
    c = Circle(10)
    t = Triangle(10, 5)

    print(f'r(w=20, h=10), area={r.area}, perimeter={r.perimeter}')
    print(f'c(r=10), area={c.area:.1f}, perimeter={c.perimeter:.1f}')
    print(f't(b=10, h=5, s=[3,4,5]), area={t.area}, perimeter={Triangle.perimeter(3,4,5)}')

App.main()