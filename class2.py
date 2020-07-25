class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

x = Person('Bibek',13)

str = ('%s aged %d lives at nepal'% (x.name,x.age))

print(str)
        