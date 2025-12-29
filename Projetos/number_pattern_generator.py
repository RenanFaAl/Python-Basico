def number_pattern(n):
    if not isinstance(n,int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    return ' '.join([str(i) for i in range(1, n+1)])  # cria uma string com separador e utiliza o for dentro dele, fazendo começar o i, sendo string, como 1 até o valor de n + 1


def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    string = ''
    for i in range(1, n + 1):
        string += str(i) + " "
    return string.strip()

print(number_pattern(4))

