def binarySearch (arr, l, r, x):

    # Check base case
    if r >= l:

        mid = l + (r - l) // 2 # If element is present at the middle itself
        if arr[mid] == x:
            return mid


        elif arr[mid] > x:  # If element is smaller than mid, then it
            return binarySearch(arr, l, mid-1, x)  # can only be present in left subarray


        else:  # Else the element can only be present
            return binarySearch(arr, mid + 1, r, x) # in right subarray
    else:
        return -1 # Element is not present in the array

x=[1,2,3]
a=binarySearch(x,0,len(x)-1,3)
print(a)