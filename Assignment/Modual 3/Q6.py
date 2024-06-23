list=['hello','univers','foof','tops','is','python','noon']

count=[]

for i in list:
    if len(i)>=2 and i[0] == i[-1]:
        count.append(i)

print(count)