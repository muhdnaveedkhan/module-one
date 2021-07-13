#Insertion sort program

numList = [5,24,78,66,42,25,38,34,18,49]
lenList = len(numList) 

for i in range(1, lenList):
    c = i
    while numList[c] < numList[c-1]:
        temp = numList[c]
        numList[c] = numList[c-1]
        numList[c-1] = temp
        c = c - 1
print(numList)