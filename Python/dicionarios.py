"""
Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. Cada elemento em um dicionário consiste em uma chave única e seu valor correspondente. Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgulas.

    Métodos de dicionários

Os dicionários em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

    keys(): retorna uma visualização de todas as chaves do dicionário.
    values(): retorna uma visualização de todos os valores do dicionário.
    items(): retorna uma visualização de todos os pares chave-valor do dicionário.
    update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.

"""

pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}

# print(pessoa["nome"]) 
# print(pessoa["idade"])   
# print(pessoa["cidade"])


print(pessoa.keys())    # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())  # Imprime dict_values(["João", 25, "Madri"])
print(pessoa.items())   # Imprime dict_items([("nome", "João"), ("idade", 25), ("cidade", "Madri")])

pessoa.update({"profissao": "Engenheiro"})
print(pessoa)  # Imprime {"nome": "João", "idade": 25, "cidade": "Madri", "profissao": "Engenheiro"}

