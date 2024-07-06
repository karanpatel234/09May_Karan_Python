class circle:

    def cac_area(self):
        pi=3.14
        radius=int(input('Enter value of Radius: '))

        area= pi * (radius*radius)

        print(f'Area of Circle: {area}')

    def cac_perimeter(self):
        pi=3.14
        radius=int(input('Enter value of Radius: '))

        perimeter= 2 * pi * radius

        print(f'Perimeter of Circle: {perimeter}')

cr=circle()

cr.cac_area()
cr.cac_perimeter()