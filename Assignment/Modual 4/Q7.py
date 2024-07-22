file = open('file_nm.txt','a')

file = open('file_nm.txt','r')

list_data=file.readlines()

all_data=f"{''.join(list_data)}"

print(all_data)