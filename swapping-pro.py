'''
#Program 1: Swaping two numbers by
	- using third variable
	- using + and -
	- using * and /
	- using bitwise xor (^)
	- using python construct
'''


"""
#   - using third variable
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Before swapping")
print("Value of a = " , a)
print("Value of b = ", b)

#logic part
t = a 
a = b
b = t

print("After swapping")
print("Value of a = " , a)
print("Value of b = ", b)
"""


"""
#   - using + and -

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("-----------------Before swapping------------")
print("Value of a = " , a)
print("Value of b = ", b)

#logic part

a = a + b
b = a - b
a = a - b

print("-----------------Before swapping------------")
print("Value of a = " , a)
print("Value of b = ", b)

"""



"""
#   - using * and /
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("-----------------Before swapping------------")
print("Value of a = " , a)
print("Value of b = ", b)

#logic part

a = a * b
b = a / b   #We can also use floor division: //
a = a / b

print("-----------------Before swapping------------")
print("Value of a = " , a)
print("Value of b = ", b)
"""

"""
#	- using bitwise xor (^)

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Before swapping")
print("Value of a = " , a)
print("Value of b = ", b)

#logic part (bitwise xor operator)
# if 1's in even numbers then result would be also 1
# if 1's in odd numbers then result would be 0

a = a ^ b       #101 ^ 110 = 100
b = a ^ b
a = a ^ b


print("-----------------Before swapping------------")
print("Value of a = " , a)
print("Value of b = ", b)

"""

#	- using python construct

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("Before swapping")
print("Value of a = " , a)
print("Value of b = ", b)

# like a, b, c = 2, 8, 3
a, b = b, a


print("-----------------Before swapping------------")
print("Value of a = " , a)
print("Value of b = ", b)