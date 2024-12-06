A = [2, 4, 7, 13, 14, 15, 16]
B = [1, 6, 7, 11, 13, 16, 18]
C = []
D = []


uniao = []
for a in A:
    if a not in uniao:
        uniao.append(a)
for b in B:
    if b not in uniao:
        uniao.append(b)
print(uniao)


for a in A:
    if a in B:                 
        C.append(a)
print(C)


for a in A:
    if a not in B:              
        D.append(a)
print(D)
