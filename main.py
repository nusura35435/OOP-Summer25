class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("nusura", 22)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age, address):
    self.name = name
    self.age = age
    self.address = address

p1 = Person("nusura", 22, "libijska16")

print(p1.name)
print(p1.age)
print(p1.address)