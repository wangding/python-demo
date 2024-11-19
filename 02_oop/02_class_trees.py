class C2:  # Make superclass objects
  def x(self):
    print('C2.x')

  def z(self):
    print('C2.z')

class C3:
  def w(self):
    print('C3.w')

  def z(self):
    print('C3:z')
  
class C1(C2, C3):  # Make class C1 and linked to superclasses (in this order)
  def x(self):
    print('C1.x')

  def y(self):
    print('C1.y')

  def setname(self, who):  # Assign name: C1.setname
    self.name = who  # Self is either I1 or I2

I1 = C1()  # Make instance objects I1 and linked to their classes C1
I2 = C1()  # Make instance objects I2 and linked to their classes C1

# print(I1.name)  # AttributeError: 'C1' object has no attribute 'name'
# print(I2.name)  # AttributeError: 'C1' object has no attribute 'name'

I1.setname('bob')  # Sets I1.name to 'bob'
I2.setname('suel') # Sets I2.name to 'sue'

print(I1.name)
print(I2.name)

I1.x()  # x from C1 not C2
I2.x()

I1.y()  # y from C1
I2.y()

I1.z()  # z from C2 not C3
I2.z()