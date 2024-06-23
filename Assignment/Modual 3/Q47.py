# Sample string: 'w3resource' 
# Expected output: 
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 

str='w3resource'

dict={}

for i in str:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print(f'String: {str}')

print(dict)