test=[]

ch=int(input("Enter number of data: "))

for i in range(ch):
    number=int(input("Enter Any Number: "))
    test.append(number)

test1=tuple(test)

print(test1)

check=int(input("Enter Number to Check: "))

if check in test1:
    print(f"{check} Number is exits in tuple")
else:
    print(f"{check} Number is Not exits in tuple")