""" Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string."""

string="Krupal Patel"

seprate=string.split()

f_str=seprate[0]

s_str=seprate[1]

replace_str_x=f_str.replace("Kr","rK")

replace_str_y=s_str.replace("Pa","aP")

print(replace_str_x)

print(replace_str_y)