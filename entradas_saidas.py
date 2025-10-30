nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")


print("Olá, " + nome + "!")
print("Você tem " + idade + " anos.")

"""
A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita utilizando funções como int() ou float().
"""

idade = int(input("Insira sua idade: "))


if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

nome2 = 'Juan'
idade2 = 25

print(f"Olá, seu nome é {nome2} e tem {idade2}")