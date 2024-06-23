d1= {'1': ['a','b'], '2': ['c','d']}

print(f'Dict: {d1}\n')
print('Expected Output:')

d2=[]

for i in d1.values():
    d2.append(i)

lenth=len(d2)

for j in range(lenth):
    for k in range(lenth):
        x=d2[0][j]+d2[1][k]
        print(x,end=" ")