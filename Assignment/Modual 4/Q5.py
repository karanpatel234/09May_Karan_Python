file=open('file_name.txt','a')

file=open('file_name.txt','r')

n=int(input('How many Last lines You want to read?: '))

list_data=file.readlines()[-n:]


for i in list_data:
    print(i)