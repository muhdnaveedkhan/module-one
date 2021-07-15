#Program 1: Swaping two numbers by
	# - using third variable
	# - using + and -
	# - using * and /
	# - using bitwise xor (^)
	# - using python construct

#Program 2: WAP to sum of numbers from 1 to 10.
#Program 3: WAP to print a table in Multiplication steps.
#Program 4: WAP to print factorial of a number.
#Program 5: WAP to check a number is prime or not.
#Program 6: WAP to reverse a number.
#Program 7: WAP to check a number is perfect or not.
#Program 8: WAP to check a number is palindrome number.
#Program 9: WAP to check a number is Armstrong or not.
#Program 10: WAP to print Armstrong Number from 100 to 1000.
#Program 11: WAP to print Fibonacci series.
#Program 12: WAP to print Table from 2 to 10.
#Program 13: WAP to print Prime numbers between 1 to 100.
#Program 14: WAP to calculate HCF of two numbers.
#Program 15: WAP to calculate LCM of two numbers.
#Program 16: WAP to calculate HCF and LCM of two numbers.

#Program 1: WAP for swapping two numbers 
'''
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
'''

#Program 2: WAP to sum of numbers from 1 to 10.
'''
# sum = 0
# for count in range(1, 11):
#     sum = sum + count
# print("Sum of first ten numbers = ", sum)

sum = 0
count = 1
while count < 11:
    sum = sum + count
    count += 1
print("Sum of first ten numbers = ", sum)
'''

#Program 3: WAP to print a table in Multiplication steps.
'''
number = int(input("Enter a positive greate then 1 : "))
upper_lim = int(input("Enter a upper limit : "))

if number > 1:
    for count in range(1, upper_lim+1):
        table = number * count
        print(f"{number} x {count} = {table}")
else:
    print("OOPS! Enter valid bumber for Table")
'''

#Program 4: WAP to print factorial of a number.
'''
number = int(input("Enter a positive greate then 1 : "))

fact = 1

if number < 1:
    print(f"Factorial of {number} number is {fact}")
else:
    for count in range(1, number+1):
        fact = fact * count
    print(f"Factorial of {number} number is {fact}")
'''
#Program 5: WAP to check a number is prime or not.
'''
number = int(input("Enter a positive number : "))
check = 0

for count in range(2, number//2):
    if number%count == 0:
        check += 1
        break

if check == 0:       
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")
'''    
    
#Program 6: WAP to reverse a number.
'''
number = int(input("Enter a positive number : "))
reverse = 0
while number != 0:
    remainder = number % 10
    reverse = (reverse * 10) + remainder
    number = number // 10

print(f"Reverse = {reverse}")
'''
#Program 7: WAP to check a number is perfect or not.
# Def: A No is perfect if sum of its factors is equal to No.
'''
number = int(input("Enter a positive number : "))
sum = 0
for count in range(1, (number//2)+1) :
    if number%count == 0:
        sum = sum + count
if number == sum:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

'''
#Program 8: WAP to check a number is palindrome number.
#Def: A No is palindrom if its reverse is equal to original number
'''
number = int(input("Enter a positive number : "))
original_no = number
rev = 0
while number != 0:
    rem = number % 10    
    rev = rev * 10 + rem
    number = number // 10
if rev == original_no:
    print(f"{original_no} is palindrome.")
else:
    print(f"{original_no} is not palindrome.")
'''

#Program 9: WAP to check a number is Armstrong or not. 
#Armstrong number is a number that is equal to the sum of cubes of its digits. 
#For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
#this Applicable only on three-digits number
'''
number = int(input("Enter a two digit number (10 to 99) : "))
original_no = number
sum = 0
while number != 0:
    rem = number % 10    
    sum = sum + (rem * rem * rem)
    number = number // 10

if sum == original_no:
    print(f"{original_no} is Armstrong.")
else:
    print(f"{original_no} is not Armstrong.")
'''

#Program 10: WAP to print Armstrong Number from 100 to 1000.
'''
for number in range(100,1000):
    original_no = number
    sum = 0
    while number != 0:
        rem = number % 10    
        sum = sum + (rem * rem * rem)
        number = number // 10
    if sum == original_no:
        print(f"{original_no} is Armstrong.")
''' 

#Program 11: WAP to print Fibonacci series.
'''
upper_lim = int(input("Enter limit to print Fibonacci series : "))

first_no = 0
second_no = 1
next_no = 0

for count in range(1, upper_lim + 1):
    print(first_no)
    next_no = first_no + second_no
    first_no = second_no
    second_no = next_no
'''

#Program 12: WAP to print Table from 2 to 10.
'''
for i in range(2, 11):
    #print(f"value of i = {i}")
    for j in range(1, 11):
        print(i*j, end=" ")
    print("\n")
'''

#Program 13: WAP to print Prime numbers between 1 to 100.
'''
for i in range(1, 100):
    j = 2
    while (j <= i//2):
        if (i%j == 0):
            break
        j += 1
    if(j > i//2):
        print(i)

'''

#Program 14: WAP to calculate HCF of two numbers.
'''
first_no = int(input("Enter first number : "))
second_no = int(input("Enter second number : "))

small = 0
small = first_no if first_no < second_no else second_no

for i in range(small, 0, -1):
    if first_no%i == 0 and second_no%i == 0:
        print("HCF is ", i)
        break
'''

#Program 15: WAP to calculate LCM of two numbers.
'''
first_no = int(input("Enter first number : "))
second_no = int(input("Enter second number : "))

big_no = 0
big_no = first_no if first_no > second_no else second_no

for i in range(1, (first_no*second_no)+1):
    if i%first_no == 0 and i%second_no == 0:
        print("LCM is ", i)
        break
'''


#Program 16: WAP to calculate HCF and LCM of two numbers.
# LCM x HCF = first_no x second_no 
# LCM  = (first_no x second_no)/ HCF

first_no = int(input("Enter first number : "))
second_no = int(input("Enter second number : "))
small = 0
small = first_no if first_no < second_no else second_no
for i in range(small, 0, -1):
    if first_no%i == 0 and second_no%i == 0:
        print("HCF is ", i)
        print("LCM is ", (first_no*second_no)//i)
        break




'''
first_no = int(input("Enter first number : "))
second_no = int(input("Enter second number : "))
small = 0
big_no = 0
small = first_no if first_no < second_no else second_no
big_no = first_no if first_no > second_no else second_no

for i in range(small, 0, -1):
    if first_no%i == 0 and second_no%i == 0:
        print("HCF is ", i)
        break
for i in range(1, (first_no*second_no)+1):
    if i%first_no == 0 and i%second_no == 0:
        print("LCM is ", i)
        break
'''

















'''
# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
'''




























