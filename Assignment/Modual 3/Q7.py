list=[]

uniq_list=[]

ch=int(input("How Many numbers do you want to enter?: "))

for i in range(ch):
    number=int(input("Enter Any Number: "))
    list.append(number)

for i in list:
    if i not in uniq_list:
        uniq_list.append:

print(f"Before Removing Duplicates Numbers {list}\n")

print(f"After Removing Duplicates Numbers {uniq_list}")