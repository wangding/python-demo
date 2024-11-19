class Employee:  # General superclass
  def computeSalary(self):  # Common or default behaviors
    print('Employee.computeSalary')

  def giveRaise(self):
    print('Employee.giveRaise')

  def promote(self):
    print('Employee.promote')

  def retire(self):
    print('Employee.retire')

class Engineer(Employee):  # Specialized subclass
  def computeSalary(self):  # Something custom here
    print('Engineer.computeSalary')

bob = Employee()  # Default behavior
sue = Employee()  # Default behavior
tom = Engineer()  # Custom salary calculator

company = [bob, sue, tom]  # A composite object
for emp in company:
  emp.computeSalary()  # Run this object's version: default or custom