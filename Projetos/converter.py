def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(temp):
    fahrenheit = (temp * 9/5) + 32
    return fahrenheit

print(fahrenheit_to_celsius(40))
print(celsius_to_fahrenheit(30))



def km_to_mile(km):
    mile = km * 0.621371
    return mile

def mile_to_km(mile):
    km = mile * 1.60934
    return km

print(km_to_mile(10))
print(mile_to_km(10))


def real_to_dolar(real):
    dolar = real * 0.1792
    return round(dolar, 2)

def real_to_euro(real):
    euro = real * 0.1525
    return round(euro, 2)

print(real_to_dolar(100))
print(real_to_euro(10000))