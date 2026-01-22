class Parent:
    pass # Attributes and methods

class Child(Parent):
    pass # Inherits, extends, and/or overrides


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    def sound(self):
        return f'{self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  # Jack barks woof! woof!! woof!!!
print(jack.bark)  # woof! woof!! woof!!!

# Multiple Inheritance
class Parent:
    pass
    # Attributes and methods for Parent

class Child:
    pass
    # Attributes and methods for Child

class GrandChild(Parent, Child):
    pass
    # GrandChild inherits from both Parent and Child
    # GrandChild can combine or override behavior from each


class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.
print(frog.walk()) # I can walk on land