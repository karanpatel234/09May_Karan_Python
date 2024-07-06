try:
    number=int(input('Enter Number To Check Weather its odd or even: '))

    if number%2==0:
        raise EnvironmentError(number)
    print('You Enterd odd Number', number)
except ValueError:
    print('Error!...Please Enter Valid interger...')