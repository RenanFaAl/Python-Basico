# # SyntaxError: Quando o código não segue as regras de sintaxe

# print(local)
# # NameError: Quando não consegue encontrar uma variavel definida 

# 5 + "5"
# # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# # TypeError: Quando você tenta uma operação com tipos incompatíveis

# my_list = [1, 2, 3]
# print(my_list[5])
# # IndexError: list index out of range
# # Quando tenta acessar um index que não existe

# num = 42
# num.append(5)
# # AttributeError: 'int' object has no attribute 'append'
# # Quando você tenta usar um método que não existe para aquele tipo de dado


def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative


def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    process_data('abc')
except ValueError:
    print('Handled at higher level')


def parse_config(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return int(data)
    except FileNotFoundError:
        raise ValueError('Configuration file is missing') from None
    except ValueError as e:
        raise ValueError('Invalid configuration format') from e

config = parse_config('config.txt')
