"""
Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.

    Métodos de tuplas

Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas:

    count(elemento): devolve o número de vezes que um elemento aparece na tupla. 
    index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
    len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

"""

tupla = (1,2,3,2,4,2)

print(tupla[0])

print(tupla.count(2))
print(tupla.index(2,2))
print(tupla.index(2,2,4))
print(len(tupla))