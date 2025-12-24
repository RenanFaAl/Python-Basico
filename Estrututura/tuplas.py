"""
Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.

    Métodos de tuplas

Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas:

    count(elemento): devolve o número de vezes que um elemento aparece na tupla. 
    index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
    len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

"""

tupla = (1,2,3,2,4,2)

print(tupla[0]) # 1

print(tupla.count(2))       # 3
print(tupla.index(2,2))     # 3
print(tupla.index(2,2,4))   # 3
print(len(tupla)) # 6

print(tupla[-2]) # 4

dev = 'Renan'
print(tuple(dev)) # ('R', 'e', 'n', 'a', 'n')

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
# programming_languages.index('JavaScript') # Value Error
programming_languages.index('Python', 3) # 5 , pois começa a busca no index 3
programming_languages.index('Python', 2, 5) # 2 , pois começa a procurar no indice 2 e só para no 5, mas não contando ele

numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]
print(sorted(programming_languages, key=len)) # ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python'], faz o sort por tamanho de palavra, não por ordem alfabética

print(sorted(programming_languages, reverse=True)) # ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']