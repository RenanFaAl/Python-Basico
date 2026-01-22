class Cat:
   def speak(self):
       return "A cat meow"

class Bird:
   def speak(self):
       return "A bird tweet"
  
class Monkey:
   def speak(self):
       return "A monkey ooh ooh aah aah ooh ooh aah aah"

def animal_sound(animal):
   print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())

jorge = Monkey()

animal_sound(jorge) # = animal_sound(Monkey())

# Inheritance-based polymorphism.

class Animal:
   def speak(self):
       return 'Some generic sound'

class Cat(Animal):
   def speak(self):
       return 'A cat meow'

class Dog(Animal):
   def speak(self):
       return 'A dog barks woof woof'

class Monkey(Animal):
   def speak(self):
       return 'A monkey ooh ooh aah aah ooh ooh aah aah'
  
print(Cat().speak()) # A cat meow
print(Dog().speak()) # A dog barks woof woof
print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak()) # Some generic sound

animals = [Cat(), Dog(), Monkey()]

for animal in animals:
   print(animal.speak())

# Output:
# A cat meow
# A dog barks woof woof
# A monkey ooh ooh aah aah ooh ooh aah aah