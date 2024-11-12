class A: pass

a = A()

print(a)
print(a.__class__)
print(A)
print(A.mro(), '\n')

# 把类当对象来用
class rec: pass  # Empty namespace object

rec.name = 'Bob'  # Just objects with attributes
rec.age = 40
print(rec.name, rec.age)  # Like a C struct or a record

x = rec()  # Instances inherit class names
y = rec()
print(x.name, y.name)  # name is stored on the class only

x.name = 'Sue'  # But assignment changes x only
print(x.name, y.name, rec.name, '\n')

print(list(rec.__dict__))
print(list(name for name in rec.__dict__ if not name.startswith('__')))
print(list(x.__dict__.keys()))
print(list(y.__dict__.keys()))
print(x.name, x.__dict__['name'])  # Attributes present here are dict keys
                                   # But attribute fetch checks classes too
                                   # Indexing dict does not do inheritance
# print(x.age, x.__dict__['age'])  # KeyError: 'age'

def uppername(obj):
  return obj.name.upper()

print(uppername(x))

rec.method = uppername
print(x.method())
print(y.method())
print(rec.method(x))