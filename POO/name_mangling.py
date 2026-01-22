class Example:
    def __init__(self):
        self._internal = 'I can be accessed from outside the class, but should not'
        self.__private = 'You cannot access me directly from outside the class'

obj = Example()

print(obj._internal) # I can be accessed from outside the class, but should not
# print(obj.__private)  # AttributeError: 'Example' object has no 

"""
Usando o prefixo __ ativa o processo de name mangling do Python, 
que internamente renomeia o atributo adicionando um underscore e
o nome da classe como prefixo, __attribute into _ClassName__attribute
"""

class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

print(example1.__dict__)

"""
{'_internal': 'I can be accessed from outside the class, but should not',
'_Example__private': 'I cannot be accessed directly from outside the class'}
"""

print(example1._Example__private) # I cannot be accessed directly from outside the class

"""
Seu propósito é prever overriding acidental de atributos e métodos
quando se usa herança
"""


class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}

"""
Se o código não utilizasse o double underscore e ficasse self.data = 'Parent data' e self.data = 'Child data'
Isso não seria possivel sem o name mangling e ficaria {'data': 'Child data'} pois teria sido overwritten

Se uma classe for virar herança, use o double underscore
"""
