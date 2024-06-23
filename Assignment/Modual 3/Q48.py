def factorial(num):
    count=1
    if num < 0:
        print('Factorial is not Calculate to negative number.')

    elif num == 0:
        print('Factorial is not Calculate to Zero.')
    
    elif num >= 0:

        for i in range(1, num+1):
            count *= i

        print(f'The Factorial of {num} is {count}')

find_fecto=int(input('Enter number to find Fectorial: '))

factorial(find_fecto)