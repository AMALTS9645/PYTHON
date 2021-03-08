class student:


    def __init__(self,name,branch,mark):
     self.name = name
     self.branch = branch
     self.mark = mark

    def display(self):
     print ("my name is : " ,self.name ,"branch is:" ,self.branch ,"mark is:" ,self.mark)

    def __del__(self):
     print("destructor called deleted ")

stud1 = student("amal","mca",90)
stud2 = student("alex","mca",50)
stud1.display()
stud2.display()

del stud1
