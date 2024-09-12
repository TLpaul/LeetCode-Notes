list1 = [1,2,4,5]
list2 = [2,3,4,7]

newList = list1.copy()
for i in list2:
    newList.append(i)

print("Unsorted" , newList)


# bubble sort
for i in range(len(newList)):
   # print(i)
    for j  in range(len(newList)-i -1 ): # everytime the list is iteratred trhough one less element
        if newList[j] > newList[j +1 ]: # compare
            temp = newList[j] # store the place element in temp
            newList[j] = newList[j +1] # swap
            newList[j +1]= temp#swap
#-------------------------------

print("sorted", newList)
