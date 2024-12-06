tabela_equivalente = {
    'a': '4', 'A': '4',
    'e': '3', 'E': '3',
    'i': '1', 'I': '1',
    'o': '0', 'O': '0',
    't': '7', 'T': '7',
    's': '5', 'S': '5',
    'l': '1', 'L': '1',
    'g': '6', 'G': '6',
    'b': '8', 'B': '8',
    'c': '<', 'C': '<',
    'z': '2', 'Z': '2'
}

texto = input("Digite um texto para converter para leet: ")

texto_em_leet = ''
for char in texto:
    if char in tabela_equivalente:
        texto_em_leet += tabela_equivalente[char]
    else:
        texto_em_leet += char
print("Texto em leet speak:", texto_em_leet)
