import math
def circlearea():
    radius = int(input("enter the length of circle to find area"))
    area = math.pi * radius **2
    print("area of the circle :",area)
def circleperimeter():
    radius = int(input("enter the length of circle to find perimeter"))
    perimeter = 2 * math.pi * radius
    print("perimeter of the circle is :",perimeter)