#https://www.learnpython.org/en/Classes_and_Objects   (More exams)

#https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/

#Class :
#==========
#A simple example class
class Test:
     
    # A sample method 
    def fun(self):
        print("Hello")
 
# Driver code
obj = Test()
obj.fun()

#=======================
#Class and variable declaration
class MyClass:
	"This is my second class"
	a = 10 #Varible 
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)


#================


#The __init__ method and self

# A Sample class with init method
class Person:
 
    # init method or constructor 
    def __init__(self, name):
        self.name = name
 
    # Sample Method 
    def say_hi(self):
        print('Hello, my name is', self.name)
 
p = Person('Shwetanshu')
p.say_hi()
#===============================

#Class and Instance Variables (Or attributes)

# Class for Computer Science Student
class CSStudent:
 
    # Class Variable
    stream = 'cse'            
 
    # The init method or constructor
    def __init__(self, roll):
   
        # Instance Variable    
        self.roll = roll       
  
# Objects of CSStudent class
a = CSStudent(101)
b = CSStudent(102)
  
print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.roll)    # prints 101
  
# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"    


#===================================

#We can define instance variables inside normal methods also.

# Python program to show that we can create 
# instance variables inside methods
  
# Class for Computer Science Student
class CSStudent:
     
    # Class Variable
    stream = 'cse'     
     
    # The init method or constructor
    def __init__(self, roll):
         
        # Instance Variable
        self.roll = roll            
 
    # Adds an instance variable 
    def setAddress(self, address):
        self.address = address
     
    # Retrieves instance variable    
    def getAddress(self):    
        return self.address   
 
# Driver Code
a = CSStudent(101)
a.setAddress("Noida, UP")
print(a.getAddress()) 


==================================================================

#Creating an Object in Python

 obj = MyClass()

#class obj exam program

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# create a new MyClass
ob = MyClass()

# Output: <function MyClass.func at 0x000000000335B0D0>
print(MyClass.func)

# Output: <bound method MyClass.func of <__main__.MyClass object at 0x000000000332DEF0>>
print(ob.func)

# Calling function func()
# Output: Hello
ob.func()
=========================================

#Constructors in Python

class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function
# Output: 2+3j
c1.getData()

# Create another ComplexNumber object
# and create a new attribute 'attr'
c2 = ComplexNumber(5)
c2.attr = 10

# Output: (5, 0, 10)
print((c2.real, c2.imag, c2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
c1.attr
