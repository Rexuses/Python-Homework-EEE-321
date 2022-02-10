"""
Batuhan Beel
180403031
03/10/2021

"""
from InsertionSort import insertionSort
def mergeSort(list):

    middle = int(len(list)/2)
    firstList = list[:middle]
    secondList = list[middle:]
    resultList=[]

    sortedFirstList=insertionSort(firstList)
    sortedSecondList=insertionSort(secondList)

    i = 0
    j = 0
    k = 0

    while(i < len(sortedFirstList) and j < len(sortedSecondList)):
        if sortedFirstList[i] < sortedSecondList[j]:

            resultList.append(sortedFirstList[i])

            i += 1
        else:
            resultList.append(sortedSecondList[j])
            j += 1

        k += 1

    while i < len(sortedFirstList):
        resultList.append(sortedFirstList[i])
        i += 1
        k += 1

    while j < len(sortedSecondList):
        resultList.append(sortedSecondList[j])
        j += 1
        k += 1
    return resultList




