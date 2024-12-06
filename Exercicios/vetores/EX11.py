resultado = []
inicio = 0
total = len(A)
for i in range(total - 1, -1, -1):
    soma = A[i] + B[i] + inicio
    resultado.append(soma % 10)         
    inicio = soma // 10       
if inicio:
    resultado.append(inicio)
resultado.reverse()
print(resultado)
