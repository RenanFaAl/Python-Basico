def pin_extractor(poems):   # verifica varios poemas de uma vez
    secret_codes = []       # lista vazia para os códigos
    for poem in poems:      # loop para dividir em versos
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):       # loop para dividir em linhas e seus respectivos index
            words = line.split()                        # separação em palavras
            if len(words) > line_index:                 # verificação se o tamanho da lista palavras é maior que o index
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)                # coloca os códigos na lista
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
