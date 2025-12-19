
msg = "Hello World"

print(msg[::-1]) # dlroW olleH

print(msg[1:7]) # ello W

print(msg[0:11:2]) # HloWrd

print('Hello' in msg)  # True

print('hey' in msg)    # False

print(len(msg)) # 11

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World , só funciona com Strings

name = 'Renan Fabiani'
age = 19

name_and_age = name + str(age)
print(name_and_age) # Renan Fabiani19

name_N_age = f'Meu nome é {name} e tenho {age} anos de idade'
print(name_N_age) # Meu nome é Renan Fabiani e tenho 19 anos de idade

print(msg.upper()) # HELLO WORLD , retorna no upper case

print(msg.lower()) # hello world , retorna no lower case


my_string = "   hello world     "
print(my_string.strip()) # hello world, retorna espaços desnecessários existentes antes e depois das palavras

print(msg.replace('Hello', "Hi")) # Hi World , substitui palavra desejada

print(msg.split()) # ['Hello', 'World'] , separa as palavras

my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world, juntam elementos em uma string com separador 

print(msg.startswith('Hello')) # True, verifica se começa com a respectiva string

print(msg.endswith('World')) # True, verifica se termina com a respectiva string

print(msg.find('World')) # 6 , mostra a primeira ocorrencia da substring na string 

print(msg.count('l')) # 3, quantidade de vezes que certa substring aparece

print(msg.capitalize()) # Hello world, devolve a string com a primeira letra capitalizada e o resto em lower case

print(msg.isupper()) # False, verifica se a string toda está em upper case

print(msg.islower()) # False, verifica se a string toda está em lower case