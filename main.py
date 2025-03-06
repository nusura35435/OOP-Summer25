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

class Person:
  def __init__(self, first_name, second_name, index_number, nationality):
    self.first_name = first_name
    self.second_name = second_name
    self.index_number = index_number
    self.nationality = nationality

p1 = Person("nusura", "niyomukiza", "35453", "Rwanda")

print(p1.first_name)
print(p1.second_name)
print(p1.index_number)
print(p1.nationality)