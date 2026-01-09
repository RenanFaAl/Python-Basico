class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

#hasattr(object, attribute_name)  verifica se um atributo existe

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')
    

"""
name: T-shirt
price: 25
ERROR: Product is missing the required attribute: 'inventory_id'
"""