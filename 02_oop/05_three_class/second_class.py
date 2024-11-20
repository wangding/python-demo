from first_class import FirstClass  # Copy name into my scope

class SecondClass(FirstClass):  # inherits base calss：FirstClass
  def display(self):  # change display
    print('Current value = "%s"' % self.data)

if __name__ == '__main__':
  z = SecondClass()
  z.setdata(42)  # Finds setdata in FirstClass
  z.display()    # Finds overridden method in SecondClass
  print(z.__dict__)
  print(z.__class__)
  print(SecondClass.__mro__, '\n')

  x = FirstClass()  # x is still a FirstClass instance (old message)
  x.setdata(42)
  x.display()  # FirstClass.display(x)
  print(x.__dict__)
  print(x.__class__)
  print(FirstClass.__mro__)