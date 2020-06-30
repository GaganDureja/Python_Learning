#                                                      PYTHON TUTORIALS



# print any data
print("Hello World")

# indentation 
if 5 > 2:
	print("Five is greater than two")

# Below code shows error because there is no blank space so python cant understand code block
#if 5 > 2:
#print("Five is greater than two")


# Variable name starts with a alphabet or underscore and are case sensitive
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# + operator adds as math function
x = "Python is "
y = "awesome"
z =  x + y
print(z)


# Global Var
x = "awesome"

def myfunc():
	# use global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Data Types
x = "5" #returns str
y = {"name" : "John", "age" : 36} # returns dictionary
print(type(x))
print(type(y))

# Also we can specify the data type
x = bool("55.2")
print(x)
print(type(x)) 

#Number types
x = 1 #int
y = 2.8 #float
z = 1j #complex

print(type(x))
print(type(y))
print(type(z))

#Casting
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(45) # complex no can't be converted in float/int

print(x)
print(y)
print(z)


# Random number
import random

print(random.randrange(1, 10))

#String multiline: use three quotes
a = """Lorem ipsum  dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are array
print(a[15])

#slicing
b = "Hello, World!"
print(b[-6:-1])
print(b[0:5])
# string length
print(len(a))


#String Methods strip(), lower(), upper, replace, split
a = "Hello, World!"
print(a.split(", ")) #cut ,and space and seperate

#check String text is in or not
txt = "The rain in Spain stays mainly in the plain"
x = "rain" in txt
print(x)
x = "rain" not in txt
print(x)

#concatenation: adding 2 var
# to add string and number use format() function otherwise it shows error
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of itemno {} for {} dollars." #{0} {1 .. .. .} index can be used 
print(myorder.format(quantity, itemno, price))

# Escape Character: To insert special char like using quotes in a string
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# List
thislist = ["apple", "banana", "cherry"]
print(thislist)
for x in thislist: #loop through a list
	print(x)
#matrix
matrix_2 = [[1,3,2], [1,3,2], [2,3,4], [2,3,5]]
first_item = matrix_2[0]
print(first_item) # [1,3,2]
forth_item = matrix_2[3]
print(forth_item) #[2,3,5]
first_item_first_element = matrix_2[2][2] # or go to index 2 then inside 2nd go to index 2
print(first_item_first_element) # 4

# Tuple
thistuple = ("apple", "banana", "cherry")
# can't add new items but can be added by chinging it first to list add item then convert back

# Set
thisset = {"apple", "banana", "cherry"}
thisset2 = {"1", "2", "3"}
thisset3 = thisset.union(thisset2)
print(thisset3)

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": "1964"
}
for x, y in thisdict.items():
    print(x + " : " + y)


#If elif else
a = 2
b = 330

print("A > B") if a > b else print("B > A")

# three conditions
a = 330
b = 330

print("A > B") if a > b else print("A = B") if a == b else print("B > A")

# While/For loop
#range
for x in range(2, 30, 3):
  print(x) 

# Function
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#Recursion -- to call a function again and again
"""
import sys 
sys.setrecursionlimit(50) #set recursion limit, default is 1000
i = 0
def recu():
	global i
	i=i+1
	print("Function no ", i)
	recu()
recu()

import sys
print(sys.getrecursionlimit())"""  # get recursion limit



# Lambda - used to short a function
def myfunc(n):
  return lambda a : a * n
mysingle = myfunc(1)
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mysingle(11))
print(mydoubler(11))
print(mytripler(11))

#another lambda example
a = [(1,2), (4,34), (4,2)]
a.sort(key=lambda x:x[1])
print(a)


# Array -- same as lists
cars = ["Ford", "Volvo", "BMW"]

print(type(cars))

# Classes and Objects

# Inheritance

# Iterators

# Scope -- local/global
# Modules --is like a external file with .py extension containing functions and variables and we import it in another file
import module as m

m.external("Gagan")
a = m.person["age"]
print(a)
x = dir(m) #list the func and var
print(x) 

#also python have some built in modules
import platform
x = platform.system()
print(x)
 
# python Dates
import datetime
x = datetime.datetime.now()
y = x.strftime("%c")
print(y)

# python Math function
#find min() and max()
# find abs()-- absolute positive
x = pow(4, 3) # 4*4*4*
print(x)
# Also have math module for some extra functions
import math
x= math.pi
print(x)

# change json data to python
import json
#now use json.loads() 
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
#json.dumps() used to change python to json
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = "))) #sort_keys=True can also be used in here

# regular expression
import re
#search change and many more function for a string

# PIP -- some package like modules, no need to install in version 3.4 or later
#install package--Python36-32\Scripts>pip install camelcase
import camelcase

c = camelcase.CamelCase()

txt = "some text with uppercase"

print(c.hump(txt)) # uppercase

#uninstall package-- pip uninstall camelcase
#use pip list to list installed packages

# Try, except, finally
try:
  print(abc)
except NameError:
  print("Variable abc is not defined")
except:
  print("Something else went wrong")
else:
  print("Nothing went wrong") # if nothing wents wrong
finally:
  print("The 'try except' is finished") # this doesn't care about the upper statements
  #This can be useful to close objects and clean up resources
"""try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()"""



# User Input
print("Enter firstName:")
x = input()
print("Hello", x)
# or 
y = input("Enter lastName:")
print("Great", x, y)

# String Format
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars." #placeholder can be empty. 
print(myorder.format(quantity, itemno, price)) # placeholder index can be used again & again. Index can be named




#                                          PYTHON FILE HANDLING



# Open and read a file
print("readme file data:")
f = open("README.md", "r") # r-- read, 
# for other folder copy complete address (C:\Users\Gagan\Desktop\Sublime files\Python_learning)

print(f.read()) #read(43): show only 43 char # readline() -- shows one line #for x in f: print(x) same O/P
f.close() #good practice to close file

# Edit/Create a file
print("Edit the readme file")
"""f = open("README.md", "a") #a--append, x--create, w--write(previous delete if any)
f.write("Some text added via code (File Handling)")
f.close()""" #This is in coment bcoz everytime it runs it adds the data above

# Delete file
"""import os
os.remove(filename)"""
#check for file existence then delete
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
#os.rmdir(foldername) -- deletes folder if empty
