"""
Funções anônimas (lambda)

Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

"""
numbers = [1, 2, 3, 4, 5]

even_numbers = [list(filter(lambda num: num % 2 == 0, numbers))]
print(even_numbers)


quadrado = lambda x: x ** 2
print(quadrado(5))

squared_members = list(map(quadrado, numbers))
print(squared_members) # [[1, 4, 9, 16, 25]]