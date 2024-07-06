file = open('file_name.txt','a')

file = open('file_name.txt','r')

list_data=file.readlines()

all_data=f"{''.join(list_data)}"

print(all_data)