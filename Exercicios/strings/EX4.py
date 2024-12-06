digitos = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove']
numero = input("Digite um número: ")
for i in range(len(numero)):
    if i < len(numero) - 1:
        print(digitos[int(numero[i])])
    else:
        print(digitos[int(numero[i])])