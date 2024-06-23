tuple_list=[(12,25,4,3),('karan','hello','is','wow'),(12.3,4,58,6,97,8),()]

print(f'Origional List of Tuple: {tuple_list}\n')
for i in tuple_list:
    if len(i) == 0:
        tuple_list.remove(i)

print(f'Removin Empty tuple from tuple_list: {tuple_list}')