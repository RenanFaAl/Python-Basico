# a função enumerate() segue o index de um iterável e retorna um objeto enumerado

languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]


for index, language in enumerate(languages): # tem como startar o index como em enumerate(languages, 1):
    print(f'Index {index} and language {language}')
"""
Index 0 and language Spanish
Index 1 and language English
Index 2 and language Russian
Index 3 and language Chinese
"""

# zip() combina listas em pares de elementos e retorna um iterador de tuplas
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

for name, id in zip(developers, ids):
    print(f'Name: {name} Id: {id}')
"""
Name: Naomi Id: 1
Name: Dario Id: 2
Name: Jessica Id: 3
Name: Tom Id: 4
"""
    