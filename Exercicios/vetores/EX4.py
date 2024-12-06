V1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58, 29, 90, 97, 178]
V2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58, 64, 43, 88, 203]
posição = 0

for i in range(15):
    if V1[i] == V2[i]:
        posição += 1
print('É igual até a posição {}'.format(posição))
