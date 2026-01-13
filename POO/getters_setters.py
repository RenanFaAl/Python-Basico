# Properties = atuam como atributos mas se comportam como métodos, ou seja, voce consegue acessá-los com notação ponto.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Getter
    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value
    
    @radius.deleter
    def radius(self):
        print('Deleting radius...')
        del self._radius

my_circle = Circle(3)

print(my_circle.radius) # 3
print(my_circle.area) # 28.26
print('Initial radius:', my_circle.radius) # Initial radius: 3

my_circle.radius = 8
print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8


my_circle.radius # This will call the getter
my_circle.radius = 4 # This will call the setter


# Create circle object with a radius
my_circle_new = Circle(33)
print("Initial radius:", my_circle_new.radius)  # 33

# Delete the radius
# This calls the deleter
del my_circle_new.radius # Deleting radius...
print("Radius deleted!") # Radius deleted!

# Try to access radius after deletion
try:
    print(my_circle_new.radius)
except AttributeError as e:
    print("Error:", e) # Error: 'Circle' object has no attribute '_radius'
