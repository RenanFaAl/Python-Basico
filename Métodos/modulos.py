import math
from math import sqrt
import random
import datetime
import meu_modulo
import operacoes
import utilidades

# operacoes.py
resultado = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado}")

# utilidades.py
nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

#meu_modulo
meu_modulo.saudar("João")  # Imprime "Olá, João!"
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)

#random
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10

#datetime
data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual

#math
resultado = sqrt(25)
print(resultado)

resultado = math.sqrt(25)
print(resultado)

"""
Criar e utilizar pacotes

Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. Este arquivo pode estar vazio ou conter código de inicialização do pacote.

Por exemplo, criamos um diretório chamado meu_pacote com a seguinte estrutura:

meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py

Depois, podemos importar e utilizar os módulos do pacote em nosso programa.

from meu_pacote import modulo1, modulo2


modulo1.funcao1()
modulo2.funcao2()
"""