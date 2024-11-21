from classtools import AttrDisplay

class Person(AttrDisplay):
  def __init__(self, name,  job=None, pay=0): # Constructor takes three arguments
    self.name = name # Fill out fields when created
    self.job = job   # self is the new instance object
    self.pay = pay

  def lastName(self): # Behavior methods
    return self.name.split()[-1] # self is implied subject
 
  #@rangetest(percent=(0.0, 1.0)) # Use decorator to validate
  def giveRaise(self, percent):
    self.pay = int(self.pay * (1 + percent)) # Must change here only

  #def __repr__(self): # Added method
  #  return '[Person: %s, %s]' % (self.name, self.pay) # String to print

if __name__ == '__main__':
  bob = Person('Bob Smith') # Test the class
  sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
  print(bob.name, bob.pay) # Fetch attached attributes
  print(sue.name, sue.pay) # sue's and bob's attrs differ
  print(bob.lastName(), sue.lastName()) # Use the new methods
  sue.giveRaise(.10) # instead of hardcoding
  print(sue.pay)
  print(bob)
  print(sue)