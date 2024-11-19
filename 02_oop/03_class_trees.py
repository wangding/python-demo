class C2:
  def x(self):
    print('C2.x')

  def z(self):
    print('C2.z')

class C3:
  def w(self):
    print('C3.w')

  def z(self):
    print('C3:z')

class C1(C2, C3):
  def __init__(self, who):  # Set name when constructed
    self.name = who  # Self is either I1 or I2

  def x(self):
    print('C1.x')

  def y(self):
    print('C1.y')

I1 = C1('bob') # Make instance objects I1 and linked to their classes C1
               # and set I1.name to 'bob'
I2 = C1('suel')

print(I1.name)
print(I2.name)

I1.x()
I2.x()

I1.y()
I2.y()

I1.z()
I2.z()