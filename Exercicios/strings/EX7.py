frase1 = input("Digite a primeira string: ")
frase2 = input("Digite a segunda string: ")

frase1 = frase1.lower()
frase2 = frase2.lower()
if len(frase1) != len(frase2):
    print("As strings não são anagramas.")
else:
    contador1 = {}
    contador2 = {}

    for l_etra in frase1:
        if l_etra in contador1:
            contador1[l_etra] += 1
        else:
            contador1[l_etra] = 1

    for letra in frase2:
        if letra in contador2:
            contador2[letra] += 1
        else:
            contador2[letra] = 1

    if contador1 == contador2:
        print("As strings são anagramas.")
    else:
        print("As strings não são anagramas.")
