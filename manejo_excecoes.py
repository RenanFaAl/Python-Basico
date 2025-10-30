"""
Try

O bloco try contém o código que pode gerar uma exceção. Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.
"""
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")


"""
Except

O bloco except especifica o tipo de exceção que se deseja capturar e lidar. Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.
"""
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Valor inválido")

"""
Finally

O bloco finally é opcional e é executado sempre, independentemente de ter ocorrido uma exceção ou não. É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.
"""
try:
    # Código que pode gerar uma exceção
    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção

# Exceções Personalizadas

def funcao():
    # Código que pode gerar uma exceção personalizada
    condicao = True
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")