import random

contador = 0
while contador < 3:
    print(contador)
    contador+=1

frutas = ['banana' , 'maçã' , 'abacaxi']

for fruta in frutas:
    print(fruta)

# range (start, stop, step), quando apenas um é range(stop)

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

categories = ['Fruta', 'Vegetal']
foods = ['apple', 'carrot', 'banana']

for category in categories:
    for food in foods:
        print(category, food)


secret_number = random.randint(1,6)
guess = 0

# while guess != secret_number:
#     guess = int(input('Guess the number (1-6)'))
#     if guess != secret_number:
#         print('Try Again')

# print('You got it')

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names: # ele pula o elemento 'Naomi
    if developer == 'Naomi':
        continue
    print(developer)


for developer in developer_names: # quando aparecer naomi ele para o loop, apenas resultando em Jess
    if developer == 'Naomi':
        break
    print(developer)

    words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

