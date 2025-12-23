def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

int1 = 50
int2 = 10

print(type(int1)) # <class 'int'>
print(type(int2)) # <class 'int'>

soma_ints = int1 + int2
sub_ints = int1 - int2
mult_ints = int1 * int2
div_ints = int1 / int2

print('Soma: ', soma_ints)          # Soma:  60
print('Subtração: ', sub_ints)      # Subtração:  40
print('Multiplicação: ', mult_ints) # Multiplicação:  500
print('Divisão: ', div_ints)        # Divisão:  5.0

float1 = 5.4
float2 = -12.0

soma_float = float1 + float2
sub_float = float1 - float2
mult_float = float1 * float2
div_float = float1 / float2

print('Soma: ', soma_float)         # Soma:  -6.6
print('Subtração: ', sub_float)     # Subtração:  17.4 , - com - = +
print('Multiplicação: ', mult_float)# Multiplicação:  -64.80000000000001
print('Divisão: ', div_float)       # Divisão:  -0.45

modulo_ints = int1 % int2
modulo_float = float1 % float2

print("Integer Modulo: ", modulo_ints) # Integer Modulo:  0
print("Float Modulo: ", modulo_float)  # Float Modulo:  -6.6

floor_ints = int1 // int2
floor_float = float1 // float2

print("Integer Floor: ", floor_ints) # Integer Floor:  5
print("Float Floor: ", floor_float)  # Float Floor:  -1.0


exp_ints = int1 ** int2
exp_float = float1 ** float2

print("Integer Exponencial: ", exp_ints) # Integer Exponencial:  97656250000000000
print("Float Exponencial: ", exp_float)  # Float Exponencial:  1.62657795541398e-09

float3 = 12.90348
int3 = int(float3)

print(int3) # 12

str_int = '45'
str_float = ' 7.8'

converted_int = int(str_int)
converted_float = float(str_float)

print(converted_int, type(converted_int))       # 45 <class 'int'>
print(converted_float, type(converted_float))   # 7.8 <class 'float'> 

absolute_value = abs(float2) # float2 = -12.0
print(absolute_value) # 12.0

int4 = 56

print(round(float3))

"""

bin(): Converte um inteiro para sua representação binaria como uma String.

oct(): Converte um inteiro para sua representação octal como uma String..

hex(): Converte um inteiro para sua representação hexadecimal como uma String.

"""


binary_representation = bin(int4)
print(binary_representation)  # 0b111000

octal_representation = oct(int4)
print(octal_representation) # 0o70

hex_representation = hex(int4)
print(hex_representation) # 0x38

# pow(): Aumenta o número até a potencia do outro ou faz uma exponenciação modular.

result1 = pow(2, 3) # 2 ** 3
print(result1) # 8

result2 = pow(2, 3, 5) # (2 ** 3) % 5
print(result2) # 3

