frase = input('Informe uma frase:')
espaco = 0
a = 0
e = 0
i = 0
o = 0
u = 0

for caractere in frase:
    if caractere == ' ':
        espaco += 1
    elif caractere in ['a', 'A']:
        a += 1
    elif caractere in ['e', 'E']:
        e += 1
    elif caractere in ['i', 'I']:
        i += 1
    elif caractere in ['o', 'O']:
        o += 1
    elif caractere in ['u', 'U']:
        u += 1

print(f"Espaços :{espaco}")
print(f"Quantidade de vogais {a + e + i + o + u}")
print(f"A:{a}, E:{e}, I:{i}, O:{o}, U:{u}")
