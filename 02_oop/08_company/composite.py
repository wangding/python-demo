from person import Person

class Manager:
  def __init__(self, name, pay):
    self.person = Person(name, 'mgr', pay) # Embed a Person object
 
  def giveRaise(self, percent, bonus=.10):
    self.person.giveRaise(percent + bonus) # Intercept and delegate
 
  def __getattr__(self, attr):
    return getattr(self.person, attr) # Delegate all other attrs
 
  def __repr__(self):
    return str(self.person) # Must overload again (in 3.X)


if __name__ == '__main__':
  tom = Manager('Tom Jones', 50000) # Make a Manager: __init__
  print(tom.lastName(), tom.pay) # Runs inherited method
  tom.giveRaise(.10) # Runs custom version
  print(tom) # Runs inherited __repr__

  bob = Person('Bob Smith') # Test the class
  sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically

  print('--All three--')
  for obj in (bob, sue, tom): # Process objects generically
    obj.giveRaise(.10) # Run this object's giveRaise
    print(obj) # Run the common __repr__