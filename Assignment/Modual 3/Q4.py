list=[]
sum=0

ch=int(input("How many numbers do you want to enter?: "))

for i in range(ch):
    number=int(input("Input intger number: "))
    list.append(number)

max_number=max(list) #return max number
print(f"Largest Number From List is {max_number}\n")

list.sort() #sorting list(small to large)
small_number=list[0] #return small number
print(f"smallest Number From List is {small_number}\n")


for i in list:
    sum=sum+i #return sum of all from list

print(f"sum of all Numbers is {sum}\n")