d1 = {'a': 100, 'b': 200, 'c':300, 'd':200} 

d2=[]

for i,j in d1.items():
    if j not in d2:
        d2.append(j)

print(f'Dict: {d1}\n')

print(f'Unique Value in Dictionary: {d2}')