# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MfxEJLLLLEBheH1Vpv4H1TVMH7Nnm8Z8

**program 2**

Display future leap years from current year to a final year entered by user.
"""

y = int (input("Enter the final year:"))
print("Future leap years from 2021:")
for x in range(2021 , y+10):
 if(x%4==0) and (x%100!=0) or (x%400==0):
    print(x)

"""**program 3**

a.Generate positive list of numbers from a given list of integers
"""

NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("\nPositive Numbers in this List are : ")
for j in range(Number):
    if(NumList[j] >= 0):
        print(NumList[j], end = '   ')

"""b.Square of N numbers"""

numbers = [1, 2, 3, 4, 5]

squared_numbers = [number ** 2 for number in numbers]

print(squared_numbers)

"""c.Form a list of vowels selected from a given word"""

element = input("Enter any statement : ")
vowels =['a','e','i','o','u']
list1=[]
for x in element:
    if (x in vowels and x not in list1):
        list1.append(x)
print("Vowels present in given statement : ",list1)

"""**program4**"""

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))

"""**program 5**"""

x = []
n = int(input("enter any integers:")) 
for i in range(1, n+1):
    a = int[n]
  if (a>100):
    x.append('over')
  else:
     x.append(a)
print("modified list:", x)

"""**program 6**"""

name = input("enter the name")
list = []
count = 0
for x in name:
   list.append(x)
   if (x in name and x == 'a'):
      count = count + 1
print(count)

"""**program 7**

a
"""

list1 = [1, 2, 4, 3, 8]
list2 = [1, 2, 4, 3, 5]
print ("the first list is :" + str(list1))
print ("the second list is :" + str(list2))
l1 = len(list1)
l2 = len(list2)
print("length of list1 :", l1 , "and length of list2 :", l2)
if l1 == l2:
   print ("list are same length")
else :
    print ("list are of different length")

"""b"""

list1 = [1, 2, 4, 3, 8]
list2 = [1, 2, 4, 3, 5]
print ("the first list is :" + str(list1))
print ("the second list is :" + str(list2))
sum1 = 0
sum2 = 0
for x in range(0, len(list1)):
    sum1 = sum1 + list1[x]
print ("sum of all elements in given list1 :", sum1)
for x in range(0, len(list2)):
   sum2 = sum2 + list2[x]   
print ("sum of all elements in given list2 :", sum2)
if ( sum1 == sum2):
   print ("list sum to same value") 
else:
   print("list are of different sum")

"""c"""

list1 = [1, 2, 4, 3, 8]
list2 = [1, 2, 4, 3, 5]
print ("the first  list is :" + str(list1))
print ("the second list is :" + str(list2))
print ("the values occur in both lists :")
for x in list1:
   if(x in list1 and x in list2):
      print(x)

"""**program 8**"""

lis = []
s=input("Enter String")
for ch in s:
    if ch in lis:
        lis.append('$')
    else:
        lis.append (ch)
print(''.join(str(i) for i in lis))

"""**program 9**"""

a = input("enter a string")
print("\nnew string :")
print(a[-1:] + a[1:-1] + a[0])

"""**program 10**"""

PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
area = PI * radius * radius

print(" Area Of a Circle = %.2f" %area)

"""**program11**"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)

"""**program12**"""

n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)

"""**program 13**"""

color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[3]))

"""**program 14**"""

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)

"""**program 15**"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))

"""**program 16**"""

first_string = input()
second_string = input()

swap_string = second_string + ' ' + first_string
print(swap_string)

"""**program 17**"""

d = { 5: 1 , 4: 2 , 3: 3 , 2: 4 , 1: 5 }
 
print("The original dictionary: ", d)
 
a = dict(sorted(d.items(), key=lambda x: x[0]))
 
print("After sorting by key: ", a)

"""**program 18**"""

def Merge(dict1, dict2):
    return(dict2.update(dict1))
     

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(Merge(dict1, dict2))

print(dict2)

"""**program 19**"""

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
i = 1
while(i <= num1 and i <= num2):
  if(num1 % i == 0 and num2 % i == 0):
    gcd = i
  i = i + 1
print("GCD is", gcd)

"""**program 20**"""

list = [11, 22, 33, 44, 55]
print("Original list :",list)
for i in list:
   if(i%2 == 0):
      list.remove(i)
print("List after removing Even numbers : ", list)