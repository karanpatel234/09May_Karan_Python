tuple_list=[(12,25,4,3),('Tops','is','hello','wow'),(12.3,4,58,6,97,8)]

count=1

for i in tuple_list:
    print(f'List {count}: {list(i)}')
    count+=1