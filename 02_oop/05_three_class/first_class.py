class FirstClass:  # Define a class object
  def setdata(self, value):  # Define class's methods
    self.data = value   # self is the instance

  def display(self):
    print(self.data)   # self.data: per instance

if __name__ == '__main__':
  x = FirstClass()  # Make two instances
  y = FirstClass()  # Each is a new namespace

  x.setdata("King Arthur")  # Call methods: self is x
  y.setdata(3.14159)  # Equal: FirstClass.setdata(y, 3.14159)
  #FirstClass.setdata(y, 3.14159)

  x.display()  # self.data differs in each instance
  y.display()  # Equal: FirstClass.display(y)
  #FirstClass.display(y)

  x.data = "New value"  # Can get/set attributes outside the class too
  x.display()

  x.anothername = "spam"  # Can set new attributes here too!
  print(x.__dict__)
  print(x.__class__)  # Instance to class link

  print(FirstClass.__base__)  # Class to superclasses link