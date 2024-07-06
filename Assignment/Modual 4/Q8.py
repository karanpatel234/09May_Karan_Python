file=open('file_name.txt','r')
data=file.readlines()
string=''
for i in data:
    if i != ' ':
        string=i

list=string.split()

f_index=len(list[0])

for i in range(len(list)):
    if len(list[i]) > f_index:   
        f_index = len(list[i])
        long_word = f_index
    
for i in range(len(list)):
    if len(list[i]) == long_word:
        print(f'The Longest Word Is= {list[i]}')