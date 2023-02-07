# Comment start with # symbol
""" 
    Multi 
    line 
    comment 
"""
print("Hello world")



""""""
# Take input from user 
name=input("Enter your name: ")
#print name 
print("Hello ",name)

# accepting integer from the user
# the return type of input() function is string ,
# so we need to convert the input to integer
num1= int(input('Enter number 1: '))
num2= int(input('Enter number 2: '))

#print sum
print('Sum is: ', (num1+num2))
""""""



""""""
# Selection in python
marks=10
if(marks>10):
    print("Excellent marks scored.")
elif(marks>4):  
    print("You have passed.")
else:
    print("You have failed.")
""""""
    


""""""
# Functions in python
def myFirstFunc(arg):
    print('Here is argument passed in function: ', arg)
# Function called
myFirstFunc("Test Argument")

#WAP for main function
def getInteger():
    return int(input('Enter any integer: '))

def Main():
    print('Main function called.')
    print(getInteger())
# Check if file is ran directly(__main__) or imported(filename)? 
if __name__=="__main__":
    Main() 
""""""



""""""
# Iterations (loops)
for step in range(5):
    print(step)
""""""



""""""
# Math module example
import math
def testMath():
    num= -10
    # fabs is used to get absoulte value of a decimal
    num =math.fabs(num)
    print(num)

testMath()
""""""