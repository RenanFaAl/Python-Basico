contador = 0
while contador < 3:
    print(contador)
    contador+=1

frutas = ['banana' , 'maçã' , 'abacaxi']

for fruta in frutas:
    print(fruta)


for i in range(1,6):
    print(i*2)

cont = 0
while True:
    print(cont)
    cont += 1

    if cont == 2:
        break


for impar in range(11):
    if impar % 2 == 0:
        continue
    print(impar)