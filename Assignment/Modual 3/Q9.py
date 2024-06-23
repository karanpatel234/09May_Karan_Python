list1=[1,2,3,4,5,6]

list2=[7,8,9,10,11,12,2,1]

common_number=[]

for i in list1:
    for j in list2:
        if i is j:
            common_number.append(i)

if len(common_number) > 0:
    print("True")
else:
    print("False")