class Dog:
    species = 'Husky'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):               
        print(f"{self.name.upper()} says woof woof, I'm {self.age} years old")

# Objeto
objeto1 = Dog('Jack', 3)
objeto2 = Dog('Thatcher', 5)

objeto1.bark() # JACK says woof woof, I'm 3 years old
objeto2.bark() # THATCHER says woof woof, I'm 5 years old
print(objeto1.species)







