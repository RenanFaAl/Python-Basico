"""
As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário. As funções nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fáceis de manter.

Para definir uma função em Python, utilizamos a palavra-chave def seguida do nome da função e parênteses. Opcionalmente, podemos especificar parâmetros dentro dos parênteses. O bloco de código da função é indentado após os dois pontos.

Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses
"""

def saudacao():
    print ('Hello World')

saudacao()

def saudacaoNome(nome):
    print(f'Olá , {nome}!')

saudacaoNome('Renan')

def soma(a,b):
    return a + b

resultado = soma(5, 10)

print(resultado)

"""
Funções anônimas (lambda)

Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.
"""

quadrado = lambda x: x ** 2
print(quadrado(5))

# def funcao():
#     var_local = 10
#     print(var_local)

# var_global = 20

# def funcao2():
#     print(var_global)

# funcao()
# funcao2()
# print(var_global)
# print(var_local) gera erro


def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

print(area_retangulo(10 , 2))

"""
Funções com número variável de argumentos

Python permite definir funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador * antes do nome do parâmetro.
"""
def calcularMedia(*numeros): #* coleta os argumentos e armazena numa tupla
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("Média: " , calcularMedia( 10, 20 , 30))

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
    #return sum(numeros)

print(soma_variavel(3,4,3))