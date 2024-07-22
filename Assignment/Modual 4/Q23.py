class rectangle:

    def calculate(self):
        length=int(input('Enter Value of length: '))
        width=int(input('Enter Value of Width: '))

        area=length * width

        print(f'Area Of Rectangle is: {area}')

ra=rectangle()

ra.calculate()