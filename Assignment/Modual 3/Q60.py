def trapezoid(top,bottom,height):

    trapezoid=((top+bottom)/2)*height

    print(f'Area of a Trapezoid: {trapezoid}')


top=int(input('Enter Value of Top: '))
bottom=int(input('Enter Value of Bottom: '))
height=int(input('Enter Value of Height: '))

trapezoid(top,bottom,height)