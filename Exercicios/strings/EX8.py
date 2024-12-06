frase = input("Digite uma frase: ")
frase_transformada = ''

for letra in frase:
    if letra.islower():
        frase_transformada += letra.upper()
    elif letra.isupper():
        frase_transformada += letra.lower()
    else:
        frase_transformada += letra

print("Frase tfrase_transformada:", frase_transformada)
