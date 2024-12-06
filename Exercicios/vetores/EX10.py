notas = [9.9, 9.7, 9.8, 10, 10]
maior = notas[0]
menor = notas[0]
soma = 0

for nota in notas:            
    if nota > maior:
        maior = nota          
    if nota < menor:
        menor = nota            
    soma += nota                
media = (soma - maior - menor)/(len(notas) - 2)  
print('A média é {}'.format(media))
print('A maior nota é {}'.format(maior))
print('A menor nota é {}'.format(menor))
