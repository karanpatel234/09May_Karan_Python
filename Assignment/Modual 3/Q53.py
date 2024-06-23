import random

list=[12, 'Hello', 'World', 12.5, 'Tops', 28, 32]

tuple=(1,2,3,4,5,6,7,8,9,10)

ran_list=random.choice(list)

ran_tuple=random.choice(tuple)

print(f'List= {list}')
print(f'The Random Number From list is: {ran_list}\n')

print(f'Tuple= {tuple}')
print(f'The Random Number From Tuple is: {ran_tuple}')