class rect:


    def __init__(self, len, wid):
         self.__len = len
         self.__wid = wid

    def __lt__(self, other):
        a1 = self.__len * self.__wid
        a2 = other.__len * other.__wid
        print("The area of the first rectangle is:", a1)
        print("The area of the second rectangle is:", a2)
        if a1 < a2:
             print("The first rectangle has greater area")
        elif a1==a2:
            print("the area is equal")
        else:
            print("The second rectangle has greater area")
a = int(input("Enter the length of the first rectangle:"))
b = int(input("Enter the width of the fisrt rectangle:"))
rect1 = rect(a, b)
c = int(input("Enter the length of the second rectangle:"))
d = int(input("Enter the width of the second rectangle:"))
rect2 = rect(c, d)
print(rect1 < rect2)