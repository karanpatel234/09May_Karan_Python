# Write python program that swap two number with temp variable and without temp variable.


print("Swaping Number With using temp variable:")
a=15
b=30
print("Value of A Before Swap: ", a)
print("Value of B Before Swap: ", b)

c=a
a=b
b=c
print("Value of A After Swap: ", a)
print("Value of B After Swap: ", b)


print("Swaping Number Without using temp variable:")
x=60
y=40

print("Value of X Before Swap: ", x)
print("Value of Y Before Swap: ", y)

x,y=y,x

print("Value of X After Swap: ", x)
print("Value of Y After Swap: ", y)