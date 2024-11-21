from person import Person
from manager import Manager

class Department:
  def __init__(self, *args):
    self.members = list(args)
  
  def addMember(self, person):
    self.members.append(person)
  
  def giveRaises(self, percent):
    for person in self.members:
      person.giveRaise(percent)
  
  def showAll(self):
    for person in self.members:
      print(person)

if __name__ == '__main__':
  bob = Person('Bob Smith')
  sue = Person('Sue Jones', job='dev', pay=100000)
  tom = Manager('Tom Jones', 50000)
 
  development = Department(bob, sue) # Embed objects in a composite
  development.showAll()
  print()
  development.addMember(tom)
  development.showAll()
  print()
  development.giveRaises(.10) # Runs embedded objects' giveRaise
  development.showAll() # Runs embedded objects' __repr__