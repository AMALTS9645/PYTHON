class Rectangle:
    def __init__(self ,breadth, length):
        self.__breadth = breadth
        self.__length = length
    def area(self):
        return self.__breadth * self.__length

    def __lt__(self):
        if (rec1 < rec2):
            print("Area of Rectangle 2 is greater than Rectangle 1")
        elif (rec1 == rec2):
            print("Area of Rectangle 1 is equal to Rectangle 2")
        else:
            print("Area of Rectangle 1 is greater than Rectangle 2")
print("Rectangle 1")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
obj=Rectangle(a,b)

print("Area 1 = ",obj.area())

print("Rectangle 2")
a=int(input("enter the length:"))
b= int(input("enter the breadth:"))
ob=Rectangle(a,b)

print("Area 2= ",ob.area())
rec1 = obj.area()
rec2 = ob.area()
recc = Rectangle(rec1,rec2)
recc.__lt__()
