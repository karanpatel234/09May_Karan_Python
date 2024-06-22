# Write a Python function to reverses a string if its length is a multiple of 4.


a=input("Enter Any Word: ")

str_length=len(a)

if str_length % 4 == 0:
    print(a[::-1])