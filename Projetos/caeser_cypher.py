def caesar(text, shift, encrypt=True): #text = texto a ser modificado, shift = mudança da criptografia, quantos algarismos vai pular

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift] # junta os elementos faltando para o alfabeto modificado
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()) # Faz a tradução desde algarismos em upper a lower case
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13) # Courage is found in unlikely places.
print(decrypted_text)

encrypt_text = encrypt('Learning Python', 8) # Tmizvqvo Xgbpwv
print(encrypt_text)