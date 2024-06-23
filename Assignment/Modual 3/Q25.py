list=[]

ch=int(input('Enter number of data: '))

for i in range(ch):
    car=input('Enter Your Car Name: ')
    list.append(car)

tuple_list=tuple(list)

reverse_tuple=tuple_list[::-1]

print(f'Origional Tuple: {tuple_list}\n')

print(f'Tuple After Reverse original Tuple: {reverse_tuple}')