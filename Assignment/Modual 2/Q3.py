# Write a Python program to get the Fibonacci series of given range. How memory is managed in Python?


n=int(input("enter your number:"))
a=0
b=1
c=0

for i in range(n):
    print(c, end='')
    a=b
    b=c
    c=a+b
    