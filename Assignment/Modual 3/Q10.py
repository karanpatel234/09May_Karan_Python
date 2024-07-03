first_5=[]
last_5=[]

for i in range(1,31):
    if i <=5:
        square=i*i
        first_5.append(square)

    if i > 25:
        square=i*i
        last_5.append(square)
        

print(f'Squre Of First Five Number is: {first_5}\n')
print(f'Squre Of Last Five Number is: {last_5}')