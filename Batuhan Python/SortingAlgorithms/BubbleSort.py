"""
Batuhan Beel
180403031
03/10/2021

"""
def bubbleSort(list):
    for i in range(1,len(list)):
        for j in range(len(list)-i):
            if(list[j]>list[j+1]):
                list[j],list[j+1] = list[j+1],list[j]
    return list

