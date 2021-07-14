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
    
    
