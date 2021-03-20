import math
def areasphere():
    radius = float(input("enter the radius of the sphere to find area"))
    area = 4 * math.pi * radius **2
    print("area of the sphere is:",area)
def perimetersphere():
    radius = float(input("enter the radius of sphere to find perimeter"))
    perimeter = ((4/3) * math.pi * radius **3)
    print("perimeter of the sphere is:",perimeter)
