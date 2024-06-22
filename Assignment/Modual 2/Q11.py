# Write a python program to sum of the first n positive integers.


n=int(input("Input an integer Number: "))
j=0
for i in range(n):
    i+=1
    j=j+i

print("Sum Of the  Positive Integers:",j)
