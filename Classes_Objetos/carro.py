class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model) # Toyota Corolla
print(car_2.model) # Lamborghini Revuelto

print(car_1.color) # red
print(car_2.color) # green