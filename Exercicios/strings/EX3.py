codigo = input("Informe um código de 5 dígitos: ")
if len(codigo) != 5:
    print("Erro: O código deve ter exatamente 5 dígitos numéricos.")
else:
    A = int(codigo[0])
    B = int(codigo[1])
    C = int(codigo[2])
    D = int(codigo[3])
    E = int(codigo[4])
    S = 6 * A + 5 * B + 4 * C + 3 * D + 2 * E

    
    DigitoV = S % 7
    print(f"O dígito verificador para o código {codigo} é: {DigitoV}")
