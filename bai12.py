class Person:
    name = "Person"

    def __init__(self, name=None):
        self.name = name


jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))

cong = Person()
cong.name = "Congthanh"

print("%s name is %s" % (Person.name, cong.name))
