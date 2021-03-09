class rectangle():


        def __init__(self, breadth, length):
            self.breadth = breadth
            self.length = length


        def area(self):
            return self.breadth * self.length

        def area1(self):
            return self.breadth * self.length

        def perimeter(self):
            return 2 * (self.breadth + self.length)

        def perimeter1(self):
            return 2* (self.breadth + self.length)




a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))

c = int(input("enter length of second rectange:"))
d = int(input("enter the breadth of the 2nd rectangle:"))
obj = rectangle(a, b)
obj1 = rectangle(c, d)

print("Area of first rectangle:", obj.area())
print("area of second rectangle:", obj1.area1())

print("perimeter of first rectangle:", obj.perimeter())
print("perimeter of second rectangle:", obj1.perimeter())

p = obj.area()
q = obj1.area1()
if(p<q):
    print("area of second rectangle is greater than first")
else:
    print("area of first rectangle is greater than second")









