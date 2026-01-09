class Cart:
    def __init__(self):
        self.items=[]

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')
    
    def list_items(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def __iter__(self):
        return iter(self.items)
    

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' \n') # Laptop Wireless mouse Ergo keyboard Monitor, iter

print(len(cart)) # 4 , len
print(cart[3]) # Monitor , getitem

print('Monitor' in cart) # True , contains
print('banana' in cart) # False

cart.remove('Ergo keyboard')  

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart

#Aritmetico: add para soma, sub para subtração, mul para multiplicação, truediv para divisão

#String: add para concatenação, mul para repetição, format para formatar, repr para conversão de texto

#Comparação: eq para igualdade, lt para menor que, gt para maior que

#Iteração: iter para retornar um iterador, next para dar fetch mo proximo item
