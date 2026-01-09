class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

person = Person('John Doe', 30) 
 
print(getattr(person, 'name')) # John Doe 
print(getattr(person, 'age')) # 30 
print(getattr(person, 'city', 'Milano')) # Milano

attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))
# se o usuario digitar um atributo que existe, ele recebe o seu valor, se não a mensagem aparecerá
# Ex: input = name, vai printar 'John Doe'

# dir() retorna todas as propriedades e métodos de um objeto, até mesmo os built-in como __init__
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)): 
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# getattr(object, attribute_name, default_value), le um atributo mesmo que você não saiba seu nome até o runtime, se o atributo não existir, ira gerar um AttributeError, a não ser que você dê um valor default
# setattr(object, attribute_name, value) , igual ao getattr