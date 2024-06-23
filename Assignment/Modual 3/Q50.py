number=int(input('Enter Any number to Check Whether a Number is Perfect or Not: '))

sum=0

for i in range(1,number):
    if number%i == 0:
        sum+=i

if sum == number:
    print(f"Yes... {number} is a perfect Number")
else:
    print(f"No... {number} is Not a Perfect Number")