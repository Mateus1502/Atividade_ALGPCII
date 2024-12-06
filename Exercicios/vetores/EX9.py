a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 10, 12, 14, 16, 18]
c = []
i = 0 
j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i]) 
        i += 1          
    else:
        c.append(b[j])  
        j += 1          

c.extend(a[i:]) 


c.extend(b[j:]) 

print(c)

