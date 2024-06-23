d1 = {'a': 100, 'b': 200, 'c':300} 

d2 = {'a': 300, 'b': 200, 'd':400} 

d3={}

x=list(d1.values())
y=list(d2.values())

for i in range(len(x)):
    z = x[i] + y[i]
    for j in d1:
        d3[j] = z

print(f'Dict_1: {d1}\n')
print(f'Dict_2: {d2}\n')

print(f'New_dict: {d3}')