# ----------------- 链式调用改造前 -----------------------
person = {}

def set_name(name):
  person['name'] = name

def set_age(age):
  person['age'] = age

def print_person():
  print(f"Name: {person['name']}, Age: {person['age']}")

set_name('wangding')
set_age(22)
print_person()

# ----------------- 链式调用改造后 -----------------------
class Person:
  def __init__(self):
    self.name = None
    self.age = None

  def set_name(self, name):
    self.name = name
    return self  # 返回 self 以支持链式调用

  def set_age(self, age):
    self.age = age
    return self

  def display(self):
    print(f"Name: {self.name}, Age: {self.age}")

Person()  \
  .set_name("louying")  \
  .set_age(20)  \
  .display()