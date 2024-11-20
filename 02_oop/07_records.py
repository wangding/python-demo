# ------------- Tuple-based record ------------------------

rec = ('Bob', 40.5, ['dev', 'mgr']) # Tuple-based record
print(rec[0])

# ------------- Dictionary-based record ------------------------

rec = {}
rec['name'] = 'Bob' # Dictionary-based record
rec['age'] = 40.5 # Or {...}, dict(n=v), etc.
rec['jobs'] = ['dev', 'mgr']

print(rec['name'])

# ------------- Class-based record ------------------------

class rec: pass

rec.name = 'Bob'  # Class-based record
rec.age = 40.5
rec.jobs = ['dev', 'mgr']
print(rec.name, rec.age, rec.jobs)

# ------------- Instance-based record ------------------------

pers1 = rec()  # Instance-based records
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']

print(pers1.name, pers2.name)

# ------------- Class-based record v2 -----------------------

class Person:
  def __init__(self, name, age, jobs): # class = data + logic
    self.name = name
    self.age = age
    self.jobs = jobs

  def info(self):
    return (self.name, self.jobs)
  
rec1 = Person('Bob', 40.5, ['dev', 'mgr']) # Construction calls
rec2 = Person('Sue', 20, ['dev', 'cto'])
print(rec1.jobs, rec2.info()) # Attributes + methods

# ------------- SUMMARY -----------------------

rec = dict(name='Bob', age=40.5, jobs=['dev', 'mgr']) # Dictionaries
print(rec['name'])

rec = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']} # Dictionaries
print(rec['name'])

rec = Person('Bob', 40.5, ['dev', 'mgr']) # Named tuples
print(rec.name)