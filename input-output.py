# input (): This function first takes the input from the user and converts it into a string. The type of the returned object always will be <type ‘str’>. It does not evaluate the expression it just returns the complete statement as String. 
inp=input('This is shown to user for input:')

print(inp)

# Printing type of input value
print ("type: ", type(inp))


# raw_input(): This function works in older version (like Python 2.x). This function takes exactly what is typed from the keyboard, converts it to string, and then returns it to the variable in which we want to store it.
# g = raw_input("Enter your name : ")
# print g

# Typecast to datatype as you want
# inp2=int(input())
# inp2=float(input())
# inp2=str(input())


# Taking multiple input from user using functions
# Split() method syntax
# input().split(separator, maxsplit)
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()


# Using List comprehension : 
# List comprehension is an elegant way to define and create list in Python. We can create lists just like mathematical statements in one line only. It is also used in getting multiple inputs from a user. 
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is: ", x)
print("Second Number is: ", y)
print()


# Output in python


# Python 3 code for printing
# on the same line printing
# geeks and geeksforgeeks
# in the same line
print("geeks", end =" ")
print("geeksforgeeks")

# Using sys module print the words in single line
import sys
sys.stdout.write("GeeksforGeeks ")
sys.stdout.write("is best website for coding!")