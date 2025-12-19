"""
Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

 
Leitura de arquivos

Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura ("r"). Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().
"""


arquivo = open("dadospy.txt", "r") # o arquivo deve estar no diretório
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

arquivo2 = open("dados.txt", "w")
arquivo2.write("Olá mundo")
arquivo2.close()


#Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)