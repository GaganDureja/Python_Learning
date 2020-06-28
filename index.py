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





