# Selection sort

def select_sort(ls):
    list_count = len(ls)
    for i in range(0, list_count-1):
       for j in range(i+1, list_count): 
            if ls[i] > ls[j]: 
                temp = ls[i]
                ls[i] = ls[j]
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