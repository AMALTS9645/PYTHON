def cuboidarea():
    length = int(input("enter the length of cuboid to find area"))
    height = int(input("enter the height of cuboid to find area"))
    width = int(input("enter the width of cuboid to find area"))
    area = 2 * (length * width + length * height + width * height)
    print("area of the cuboid :",area)
def cuboidperimeter():
    length = int(input("enter the length of cuboid to find perimeter"))
    height = int(input("enter the height of cuboid to find perimeter"))
    width = int(input("enter the width of cuboid to find perimeter"))
    perimeter = 4 * (length + width + height)
    print("perimeter of the cuboid is :",perimeter)