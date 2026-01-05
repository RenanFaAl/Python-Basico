"""
Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma lista podem ser de diferentes tipos de dados e são encerrados entre colchetes [], separados por vírgulas.


Métodos de Listas:
    append(elemento): adiciona um elemento ao final da lista.
    insert(indice, elemento): insere um elemento em uma posição específica da lista.
    remove(elemento): remove a primeira ocorrência de um elemento na lista.
    pop(indice): remove e retorna o elemento em uma posição específica da lista.
    sort(): ordena os elementos da lista em ordem ascendente.
    reverse(): inverte a ordem dos elementos na lista.
"""

carros = ['ASX' , 'Corolla' , 'Veloster']

print(carros[0]) # Imprime ASX
print(carros[1]) # Imprime Corolla
print(carros[2]) # Imprime Veloster

print(carros[-1]) # Ordem ao contrario , Imprime Veloster 


carros.append('HB20') # Adiciona o elemento ao final da lista

carros.insert(0, 'Skyline') # Insere o elemento na posição indicada

carros.remove('Veloster') # Remove o elemento

carros_removido = carros.pop(2) # Remove o elemento do índice indicado
# se não for especificado o índice, ele tira o ultimo elemento
print(carros_removido)

carros.sort() # Organiza em ordem alfabética

carros.reverse() # Inverte a lista

for carro in carros:
    print(carro)

"""
Lista de Compressão
"""

numeros = [ 1,2,3,4,5]
quadrados = [x ** 2 for x in numeros if x % 2 == 0]

print(quadrados) # [4, 16]

developer = 'Renan'
print(list(developer)) # ['R', 'e', 'n', 'a', 'n']

print(len(carros)) # 3

print('ASX' in carros) # True
print('Onix' in carros) # False

ex_lista_inside = ['Renan', 19, ['Python', 'Java', 'C']]

print(ex_lista_inside[2]) # ['Python', 'Java', 'C']
print(ex_lista_inside[2][1]) # Java

ex_lista_variavel = ['Renan', 19, 'Python Developer']
name, age, job = ex_lista_variavel
# ou name, *rest = ex_lista_variavel, name = 'Renan' , rest = [19, 'Python Developer']

print(name) # 'Renan'
print(age) # 19
print(job) # 'Python Developer'

numbers = [1, 2, 3, 4, 5]

print(numbers[1:4] ) # [2, 3, 4]
print(numbers[0::2]) # [1, 3, 5]

even_number = [6, 8, 10]

numbers.extend(even_number) # parecido com append(), mas você 
# pode adicionar vários elementos de uma lista para outra
# se usasse append() ficaria assim =  [1, 2, 3, 4, 5, [6, 8, 10]]

print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

# clear() remove todos os elemetos da lista

# Refatoração

even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)

number1_to_5 = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in number1_to_5]
print(result)

soma = sum(number1_to_5)
print(soma) # 15

total = sum(number1_to_5, 10) # pode adicioanar um valor de start
print(total) # 25


words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words)) # filter() aceita uma função e um iterável, nesta ordem
print(long_words) # ['mountain', 'river', 'cloud']
# filter() seleciona itens de um iterável que batem com uma condição específica



celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit,celsius)) # igual ao filter na questão do que aceita
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]
# map() aplica uma função a cada elemento de um iterável

def mult_list(item):
    return item * 2

new_list = list(map(mult_list,celsius))

n_list = [temp * 2 for temp in celsius]

print(new_list)
print(n_list)