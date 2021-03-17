import csv
file=open("C:/Users/student.MCALAB/Desktop/20mca011/PYTHON/cycle5/pgm5.csv", 'r')
reader = csv.reader(file)
for row in reader:
    print(row)