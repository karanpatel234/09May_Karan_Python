test=(10,12,3,45,3,10,12)

list=[]

for i in test:
    if test.count(i) >= 2:
        list.append(i)

print(f'Origional Tuple: {test}\n')

print(f'Repeated items from tuple: {tuple(set(list))}')