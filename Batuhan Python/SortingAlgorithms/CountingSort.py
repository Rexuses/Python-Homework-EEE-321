#Batuhan Beel 180403031
#01.11.2021
def counting_sort(arr,min,max):
    result_arr = [0 for i in range(len(arr))]
    temp_arr = [0 for i in range(min,max+1)]
    for i in arr:
        temp_arr[i-min] +=1
    for j in range(len(temp_arr)-1):
        temp_arr[j+1] += temp_arr[j]
    for i in arr:
        result_arr[temp_arr[i-min]-1] = i
        temp_arr[i-min]-=1

    return result_arr

