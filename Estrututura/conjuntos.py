#Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos.
#Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().
frutas = {"maçã","banana","laranja"}
numeros = set([1,2,3,4,5])

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

"""

    Métodos de conjuntos

Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

    add(elemento): adiciona um elemento ao conjunto.
    remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
    discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
    clear(): remove todos os elementos do conjunto.

"""
frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()


my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print(your_set.issubset(my_set)) # False
print(my_set.issuperset(your_set)) # False

print(my_set.isdisjoint(your_set)) # False, verifica se 2 sets não tem valores em comum

my_set | your_set # {1, 2, 3, 4, 5, 6}

my_set & your_set # {2, 3, 4}

my_set - your_set # {1, 5}, retorna valores que tão em my_set, mas não em your_set

my_set ^ your_set # {1, 5, 6}, retorna elementos que são únicos entre os sets, não estando em ambos.

# |= &= -= ^=, tudo isso funciona por assigment

my_set -= your_set

print(my_set) # {1, 5}
print(5 in my_set) # {1, 5}


