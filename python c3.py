# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yU3nxoB7W7rgYwLFOva_iBjAODTco6i2

**1. Program to find the factorial of a number **
"""

num = int(input("Enter a number: "))  
factorial = 1  
if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   for i in range(1,num + 1):  
       factorial = factorial*i  
   print("The factorial of",num,"is",factorial)

"""**2.Generate Fibonacci series of N terms **


"""

n=int(input("enter the value of 'n':"))
a=0
b=1
sum=0
count=1
print("fibonacci series:",end="")
while(count<=n):
  print(sum, end="")
  count+=1
  a=b
  b=sum
  sum=a+b

"""**3.Find the sum of all items in a list **"""

def sum_list(items):
  sum_numbers = 0
  for x in items:
    sum_numbers += x
  return sum_numbers
print(sum_list([1,2,4]))

"""**4. Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.**"""

l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
   a=[]
  a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)

"""** 5. Display the given pyramid with step number accepted from user. Eg: N=4 1 2 4 3 6 9 4 8 12 16**"""

rows=5
for row in range(1,rows+1):
  for column in range (1,row+1):
    print(column,end='')
  print("")

"""**6. Count the number of characters (character frequency) in a string. **"""

def char_freaquency(str1):
  dict={}
  for n in str1:
    keys=dict.keys()
    if n in keys:
      dict[n] +=1
    else:
      dict[n] = 1
  return dict
print(char_freaquency('google.com'))