# list comprehension 
# with the help of list comprehension we can create of list in one line

# ---------------- Problem #1 : reverse the list's elements-----------
# ls = ['abc', 'xyz', 'vut', 'lms']
# new_ls = []
# for el in ls:
#     new_ls.append(el[::-1])
# print(new_ls)

# Similary, we can do the same with list comprehension
# ls = ['abc', 'xyz', 'vut', 'lms']
# new_ls = [el[::-1] for el in ls ]
# print(new_ls)

# ---------------- Problem #2 : create a  new list of even numbers from old one -----------
# list comprehension with if statement
list1 = list(range(1,11))
even_ls = []
odd_ls = []

# for el in list1:
#     if el%2 == 0:
#         even_ls.append(el)
#     else:
#         odd_ls.append(el)
# print(even_ls)
# print(odd_ls)

#Similarly, we can do the same by using list comprehension

even_ls = [el for el in list1 if el%2 == 0]
odd_ls = [el for el in list1 if el%2 != 0]
print(even_ls)
print(odd_ls)










# create a list of squres from 1 to 10
list1 = list(range(1,11))
list2 = [1,2,3,4,5,6,7,8,9,10]

sq_list = []

# for i in range(1,11):
#     sq_list.append(i**2)
# print(sq_list)

# we can create the same with list comprehension

# sq_list = [ i**2 for i in range(1,11) ]
# print(sq_list)

# negative = []
# for cnt in range(1,11):
#     negative.append(-cnt)
# print(negative)

# # Similarly, with the help of list comprehension
# negative = [-cnt for cnt in range(1,11) ]
# print(negative)


# names = ['Wasim', 'Ali' , 'Sohail', 'Faizan']
# list_name = []
# for item in names:
#     list_name.append(item[0])
# print(list_name)

# Similary with list comprehension
# names = ['Wasim', 'Ali' , 'Sohail', 'Faizan']
# list_name = [item[0] for item in names]
# print(list_name)


