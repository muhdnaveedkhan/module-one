''' ------------- Problem #3-----------'''
def printNum(num):
    for i in range(1, num+1):
        print(i, end="")
    print("\n")
    
printNum(7)




''' ------------- Problem #3-----------'''
# def is_leap(year):
#     leap = False
#     if year%4 == 0:
#         if year%100 == 0:
#             if year%400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
    
#     return leap

# print(is_leap(1000))



''' ------------- Problem #2-----------'''
# n = int(input())
# for i in range(n):
#     print(i**2)


''' ------------- Problem #1-----------'''
# n = int(input())
# if n % 2 == 0:
#     if n in range(2,6):
#         print("Not Weird")

#     elif n in range(6,21):
#         print("Weird")

#     elif n > 20:
#         print("Not Weird")
# else:
#     print("Weird")

# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}

# print(check[
#         n%2==0 and (
#             n in range(2,6) or 
#             n > 20)
#     ])

'''
num = int(input("Enter a positive integer : "))

if (num%2 != 0 or num == 1):
    print("Weird")
elif  1 < num < 6:
    print("Not Weird")
elif 5 < num < 21:
    print("Weird")
elif num > 20:
    print("Not Weird")
else:
    pass
  '''