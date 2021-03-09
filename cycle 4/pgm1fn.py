class rect:
    def __init__(self, len,wid):
        self.len=len
        self.wid=wid

    def area(self):
        self.a=self.len*self.wid
        print("The area of the rectangle is:", self.a)

    def perimeter(self):
        self.p=2*(self.len+self.wid)
        print("The perimeter of the rectangle is:",self.p)

    def __gt__(self, other):
        a1=self.len*self.wid
        a2=other.len*other.wid
        if a1>a2:
            print("The greater is the first one",a1)
        else:
            print("The greter is the second one",a2)

rect1=rect(4,6)
rect1.area()
rect2=rect(4,6)
rect2.perimeter()
rect3=rect(2,3)
rect3.area()
print(rect1>rect3)