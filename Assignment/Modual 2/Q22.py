"""Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string."""

a=input("Enter any word: ")

length=len(a)

if length < 2:
    print("")
else:
    start_char=a[:2]
    last_char=a[-2:]
    new_str=start_char + last_char
    print(new_str)