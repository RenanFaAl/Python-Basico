# Classe abstrata não pode ser instanciada, e seus métodos 
# tem que ser sobreescritos em classes que os herdarem
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print('Woof')

class Cat(Animal):
    def make_sound(self):
        print('Meow')

class Monkey(Animal):
   def make_sound(self):
       print('Ooh ooh aah aah!')

animals = [Dog(), Cat(), Monkey()]

for animal in animals:
   animal.make_sound()


"""
neste exemplo, as classes adaptam o método speak do seu jeito e devem
seguir o método init da classe abstrata
"""
class TalkingToy(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def speak(self):
        pass

class RobotToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
   def speak(self):
       print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
   def speak(self):
       print(f'{self.name} says ROOOOAR!')
        
# Create toys
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys = [rusty, fluffy, rex]
for toy in toys:
   toy.speak()