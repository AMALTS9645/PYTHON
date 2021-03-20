f = open("C:/Users/student.MCALAB/Desktop/20mca011/PYTHON/cycle5/py.txt", 'r')
f2 = open("C:/Users/student.MCALAB/Desktop/20mca011/PYTHON/cycle5/write.txt", 'w')
cont = f.readlines()
for i in range(0,len(cont)):
    if(i%2!=0):
        f2.write(cont[i])
f2 = open("write.txt", 'r')
cont1 = f2.read()
print(cont1)
f.close()
f2.close()
