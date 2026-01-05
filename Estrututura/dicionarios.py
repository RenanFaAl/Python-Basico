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

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])

print(pizza.get("price")) # 8.9
print(pizza.get("toppings", [])) # retorna ['mozzarella', 'basil'], chave e default, se a chave não existir, devolve o default

print(pizza.pop('total_price', 10)) # retorna 10, chave e default, caso não exista nenhum dos dois vai gerar KeyError

# print(pizza.popitem) remove o ultimo par adicionado
pizza.update({ 'price': 15, 'total_time': 25})

print(pizza)


products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
    print(price) # 990 600 250 70

for product in products:
    print(product) # Laptop Smartphone Tablet Headphones

for product in products.items():
    print(product) 
    """
    ('Laptop', 990)
    ('Smartphone', 600)
    ('Tablet', 250)
    ('Headphones', 70)
    """

for product, price in products.items():
    products[product] = round(price * 0.8)

print(products) # {'Laptop': 792, 'Smartphone': 480, 'Tablet': 200, 'Headphones': 56}

for index, product in enumerate(products):
    print(index, product)
    """
    0 Laptop
    1 Smartphone
    2 Tablet
    3 Headphones
    """

for index, product in enumerate(products.items()):
    print(index, product)