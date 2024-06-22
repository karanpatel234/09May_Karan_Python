# Write a Python function that takes a list of words and returns the length of the longest one.


name=["Krupal","Viraj","Kelvin","Abhisek"]

length=len(name[0])

for i in name:
    all_length = len(i)
    
    if all_length > length:
        longest_length = all_length

if len(i) == longest_length:
    print("Longest word in list is with Characters:",longest_length,i) 