a=10
b='20'

try:
    if a>b:
        print(f'Sum of A+B= {a+b}')
except Exception as e:
    print(e)
finally:
    print('Executed rest code....')