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

print(quadrados)