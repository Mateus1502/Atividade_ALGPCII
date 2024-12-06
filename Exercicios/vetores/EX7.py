matricula = []

for i in range(100):
    numero = int(input('Digite matricula: '))
    if numero in matricula:
        print('Esse valor de matricula já existe, digite outro numero')
    else:
        matricula.append(numero)
print(matricula)
