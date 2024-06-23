import random

def rand_num(num1, num2):
    ren_num=random.choice(range(num1,num2))
    print(f'Random Number From Range Between {num1} and {num2} is {ren_num}')

start_number=int(input('Enter First Number: '))
last_number=int(input('Enter Last Number: '))


rand_num(start_number,last_number)