test=[]

ch=int(input("Enter number of data: "))

for i in range(ch):
    city=input("Enter Your City Name: ")
    test.append(city)

tuple=tuple(test)

print(f'The List is: {test}\n') # Return Origional list

print(f'After convert List into tuple: {tuple}') # Return Tuple 