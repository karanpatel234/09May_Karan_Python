def cylinder(radius,height):

    surface_volume=3.14*(radius*radius)*height
    surface_area=2*3.14*(radius*radius) + 2*3.14*radius*height
    print(f'Surface Volume of Cylinder is {surface_volume}')
    print(f'Surface Volume of Area is {surface_area}')

radius=int(input('Enter Value of Radius: '))
height=int(input('Enter Value of Height: '))

cylinder(radius,height)