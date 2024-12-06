vetor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
vetor2 = [2, 4, 6, 8, 10, 12, 14, 16]
vetor3 = []
i = 0
while i < len(vetor1) or i < len(vetor2):              
    if i <len(vetor1) and i < len(vetor2):                 
        vetor3.append(vetor1[i] + vetor2[i])
    elif i < len(vetor1):                             
        vetor3.append(vetor1[i])                           
    else:
        vetor3.append(vetor2[i])                           
    i += 1
print(vetor3)
