dict_1={'Mango': 12, 'Apple':42, 'Banana':23, 'Watermelon':10, 'Papaya':14}

list=[]

for i in dict_1.values():
    list.append(i)

list.sort()

print(f'Dictionary: {dict_1}\n')

print(f'3 Max_values: {list[-3:]}')