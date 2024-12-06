vetor = []
for i in range(20):
    num = int(input(f"Digite número: "))
    vetor.append(num)
print(vetor)
for i in range(10):           
    vetor[i], vetor[19 - i] = vetor[19 - i], vetor[i]
print(vetor)

