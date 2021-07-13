# Selection sort

def select_sort(ls):
    list_count = len(ls)
    for i in range(list_count):
       for j in range(list_count - 1): 
            if ls[j+1] < ls[j]: 
                temp = ls[j+1]
                ls[j+1] = ls[j]
                ls[j] = temp
    return ls

numList = [5,2,7,66,42,25,38,34,18,49]

#calling function
sortedLs = select_sort(numList)
print(sortedLs)


# numList = [5,2,7,66,42,25,38,34,18,49]
# lenList = len(numList) 

# for i in range(lenList):
#    for j in range(lenList - 1): #We will not checking last element
#        if numList[j+1] < numList[j]: #Swap the numbers
#            temp = numList[j+1]
#            numList[j+1] = numList[j]
#            numList[j] = temp

# print(numList)