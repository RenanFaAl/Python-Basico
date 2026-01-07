# Debugging
# Usando f-strings e print nas funções
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result

#Usando módulo pdb
import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))

