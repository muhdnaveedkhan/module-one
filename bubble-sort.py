#Bubble sort program

def bubble_sort(input_ls):
    lenList = len(input_ls)
    for i in range(0, lenList):
        for j in range(0, lenList - 1): 
            if input_ls[j] > input_ls[j+1]: #Swap the numbers
                temp = input_ls[j]
                input_ls[j] = input_ls[j+1]
                input_ls[j+1] = temp
    return input_ls

numList = []
for i in range(1, 8):
    numList.append(int(input("enter 7 numbers : ")))
sortedls = bubble_sort(numList)
print(sortedls)











# numList = [5,2,7,66,42,25,38,34,18,49]
# lenList = len(numList) 

# for i in range(0, lenList):
#    for j in range(0, lenList - 1): 
#        if numList[j] > numList[j+1]: #Swap the numbers
#            temp = numList[j]
#            numList[j] = numList[j+1]
#            numList[j+1] = temp

# print(numList)