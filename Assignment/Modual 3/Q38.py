dict_1={'Id':101, 'Name':'Pankaj', 'City':'Rajkot'}

dict_key=[]

check_key=['Id','Name','City','sub']

for i in dict_1:
    dict_key.append(i)

print(f'Dict_1 Keys: {dict_key}\n')

print(f'Key_to_check: {check_key}\n')

print('Do All Keys Exist?')

if check_key == dict_key:
    print('True')
else:
    print('False')
    