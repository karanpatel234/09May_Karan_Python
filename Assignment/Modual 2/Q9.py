# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.


a=int(input("Enter Your First Number A:"))
b=int(input("Enter Your Second Number B:"))
c=int(input("Enter Your Third Number C:"))

if a==b or a==c or b==c:
    print("Sum Of A+B+C=0")
else:
    print("Sum Of A+B+C=",a+b+c)
    
    