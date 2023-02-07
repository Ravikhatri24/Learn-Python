import keyword

for kw in keyword.kwlist:
    print(kw)
    
# Check if string is keyword
print(keyword.iskeyword("sor"))
print(keyword.iskeyword("or"))


# Python returns last evaluated value in case of "and" keyword. Return the first false value. If not found return last. 
print(10 and 20)

# Python returns first evaluated value in case of "or" keyword. Return the first True value.if not found return last. 
print(10 or 20)


# Boolean checks work same as other language
print(True and False)
print(False and True)
print(True and True)
print(False and False)
print(True or False)
print(False or True)
print(True or True)
print(False or False)


# not: This logical operator inverts the truth value. The truth table for “not” is depicted below. 
print("not: ", not True)

# in: This keyword is used to check if a container contains a value. This keyword is also used to loop through the container.
# using "in" to check
if 's' in 'geeksforgeeks':
    print("s is part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")
# using "in" to loop through
for i in 'geeksforgeeks':
    print(i, end=" ")

# is: This keyword is used to test object identity, i.e to check if both the objects take the same memory location or not. 
# using is to check object identity
# string is immutable( cannot be changed once allocated)
# hence occupy same memory location
print('\n',' ' is ' ')
 
# using is to check object identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
print({} is {})


""""""
#Iteration Keywords – for, while, break, continue
#break: “break” is used to control the flow of the loop. The statement is used to break out of the loop and passes the control to the statement following immediately after loop.
#continue: “continue” is also used to control the flow of code. The keyword skips the current iteration of the loop but does not end the loop.
#for: This keyword is used to control flow and for looping.
for i in range(10):
    if i==2:
        continue
    if i==6:
        break
    print(i, end=" ")

#while: Has a similar working like “for”, used to control flow and for looping.
j=0
while j<10:
    print(j)
    j+=1
    
""""""

# Conditional keywords – if, else, elif
# if : It is a control statement for decision making. Truth expression forces control to go in “if” statement block.
# else : It is a control statement for decision making. False expression forces control to go in “else” statement block.
# elif : It is a control statement for decision making. It is short for “else if“
if(1==2):
    print("Equal")
elif 1==1:
    print("Equal in elif")
else: 
    print("Equal condition not met")
    
""""""


# def keyword
def myFunc():
    print('Hello world')
myFunc()


""""""

# Return Keywords – Return, Yield
# return : This keyword is used to return from the function.
def checkInt(arg):
    return "Hello"
print(checkInt(2))
        
# yield : This keyword is used like return statement but is used to return a generator.
# Yield Keyword
def fun():
    S = 0
     
    for i in range(10):
        S += i
        yield S
 
for i in fun():
    print(i)
    

# Lambda keyword is used to make inline returning functions with no statements allowed internally. 
i = lambda z:z*z*z
print(i(10))


# import : This statement is used to include a particular module into current program.
# from : Generally used with import, from is used to import particular functionality from the module imported.
import math
print(math.factorial(10))
 
from math import factorial
print(factorial(10))

# try : This keyword is used for exception handling, used to catch the errors in the code using the keyword except. Code in “try” block is checked, if there is any type of error, except block is executed.
# except : As explained above, this works together with “try” to catch exceptions.
# finally : No matter what is result of the “try” block, block termed “finally” is always executed.
# raise: We can raise an exception explicitly with the raise keyword
# assert: This function is used for debugging purposes. Usually used to check the correctness of code. If a statement is evaluated to be true, nothing happens, but when it is false, “AssertionError” is raised. One can also print a message with the error, separated by a comma.
a=1
b=0
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print('Division by zero so error occurred')
finally:
    print('Finally is used to execute everytime after try block')
# using assert to check for 0
print ("The value of a / b is : ")
# assert b != 0, "Divide by 0 error"  # gives error 
# print (a / b)


# del is used to delete a reference to an object. Any variable or list value can be deleted using del.
myval1=1
print(myval1)
del myval1
# print(myval1)         # gives error



# global: This keyword is used to define a variable inside the function to be of a global scope.
# non-local : This keyword works similar to the global, but rather than global, this keyword declares a variable to point to variable of outside enclosing function, in case of nested functions.
globalvar1 = 12
def testGlobalvar():
    global globalvar1  # Solves assignment error by declaring that we are going to use global variable
    globalvar2=globalvar1+5
    globalvar1 = globalvar2
    print(globalvar1)
testGlobalvar()

# nonlocal keyword
nonlocalvar1 = 122
def funnonlocalvar1():
    nonlocalvar1 = 10
    def gunnonlocalvar1():
        # tell python explicitly that it has to access var1 initialized in fun on line 2 using the keyword nonlocal
        nonlocal nonlocalvar1
         
        nonlocalvar1 = nonlocalvar1 + 10
        print("nonlocalvar1 nonlocal",nonlocalvar1)
    gunnonlocalvar1()
funnonlocalvar1()