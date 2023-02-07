# Arithmetic Operators
# + = Addition
# - = Substraction
# * = Muliplication
# / = Division(float)
# // = Division(floor)
# % = Modulus
# ** = Power: returns first raised to power second


# PRECEDENCE:
# P – Parentheses
# E – Exponentiation
# M – Multiplication     (Multiplication and division have the same precedence)
# D – Division
# A – Addition     (Addition and subtraction have the same precedence)
# S – Subtraction


# Comparison Operators
# >
# <
# ==
# !=
# <=
# >=
# is                 x is the same as y (Checks memory address is same for the object)
# is not             x is not the same as y (Checks memory address is not same for the object)


# Logical Operators
# and 
# or
# not


# Bitwise Operators 
# &	Bitwise AND 
# |	Bitwise OR	
# ~	Bitwise NOT	
# ^	Bitwise XOR	 
# >>	Bitwise right shift
# <<	Bitwise left shift


# Assignment Operators 
# =	Assign value of right side of expression to left side operand  
# +=	Add AND: Add right-side operand with left side operand and then assign to left operand	 
# -=	Subtract AND: Subtract right operand from left operand and then assign to left operand 
# *=	Multiply AND: Multiply right operand with left operand and then assign to left operand 
# /=	Divide AND: Divide left operand with right operand and then assign to left operand 
# %=	Modulus AND: Takes modulus using left and right operands and assign the result to left operand 
# //=	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand 
# **=	Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand 
# &=	Performs Bitwise AND on operands and assign value to left operand 
# |=	Performs Bitwise OR on operands and assign value to left operand 
# ^=	Performs Bitwise xOR on operands and assign value to left operand 
# >>=	Performs Bitwise right shift on operands and assign value to left operand 
# <<=	Performs Bitwise left shift on operands and assign value to left operand 



# Membership Operators
# in 
# not in
x = 24
y = 20
list = [10, 20, 30, 40, 50]
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
    

# Ternary operator
# Syntax : [on_true] if [expression] else [on_false] 


# Operator overloading
# when we use + operator, the magic method __add__ is automatically invoked in which the operation for + operator is defined.
class A:
    def __init__(self, a):
        self.a =a
        
    # overloading the binary + operator on class objects
    def __add__(self,obj):
        if(isinstance(self.a, str)):
            return self.a + " " + obj.a
        return self.a+obj.a
Obj1=A(2)
Obj2=A(22)
Obj3=A("Test")
Obj4=A("String")
print(Obj1+Obj2)
print(Obj3+Obj4)
print(isinstance("sdf", str))
# Actual working when Binary Operator is used.
# print(A.__add__(ob1 , ob2))
# print(A.__add__(ob3,ob4))
#And can also be Understand as :
# print(ob1.__add__(ob2))
# print(ob3.__add__(ob4))

# we can overload other operator and their magic methods are
# Binary operators
# +	__add__(self, other)
# –	__sub__(self, other)
# *	__mul__(self, other)
# /	__truediv__(self, other)
# //	__floordiv__(self, other)
# %	__mod__(self, other)
# **	__pow__(self, other)
# >>	__rshift__(self, other)
# <<	__lshift__(self, other)
# &	__and__(self, other)
# |	__or__(self, other)
# ^	__xor__(self, other)

# comparison operators
# <	__lt__(self, other)
# >	__gt__(self, other)
# <=	__le__(self, other)
# >=	__ge__(self, other)
# ==	__eq__(self, other)
# !=	__ne__(self, other)

# Assignment operators
# <	__lt__(self, other)
# >	__gt__(self, other)
# <=	__le__(self, other)
# >=	__ge__(self, other)
# ==	__eq__(self, other)
# !=	__ne__(self, other)

# Unary Operators
# –	__neg__(self)
# +	__pos__(self)
# ~	__invert__(self)


# "Any" "All" in python
#  Any Returns true if any of the items is True. It returns False if empty or all are false.
# Syntax :   any(list of iterables)  
# Since all are false, false is returned
print (any([False, False, False, False]))
 
# Here the method will short-circuit at the
# second item (True) and will return True.
print (any([False, True, False, False]))
 
# Here the method will short-circuit at the
# first (True) and will return True.
print (any([True, False, False, False]))

# All Returns true if all of the items are True (or if the iterable is empty)
# Syntax :   any(list of iterables)  
# Here all the iterables are True so all
# will return True and the same will be printed
print (all([True, True, True, True]))
 
# Here the method will short-circuit at the
# first item (False) and will return False.
print (all([False, True, True, False]))
 
# This statement will return False, as no
# True is found in the iterables
print (all([False, False, False]))