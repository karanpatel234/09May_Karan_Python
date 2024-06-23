tuple_1=(101,102,103,104,105)

tuple_2=('Vivan','Rahul','Hardik','Shivam','Nishan')

total=len(tuple_1)

dict_list={}

for i in range(total):
        dict_list[tuple_1[i]] = tuple_2[i]

print(dict_list)