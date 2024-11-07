class Rectangle:
  def __init__(self, width, height):
    self.__width = width
    self.__height = height

  @property
  def perimeter(self):
    return 2 * (self.__width + self.__height)

  @property
  def area(self):
    return self.__width * self.__height

rect = Rectangle(5, 10)
print(f"Area: {rect.area}")
print(f"Perimeter: {rect.perimeter}")