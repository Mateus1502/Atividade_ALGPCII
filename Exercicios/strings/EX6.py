nome=input("Informe seu nome completo")
conectores = {'do', 'da', 'dos', 'das', 'de'}
palavras = nome.split()
iniciais = ''
for palavra in palavras:
    if palavra.lower() not in conectores:
        iniciais += palavra[0].upper()
print(iniciais)
