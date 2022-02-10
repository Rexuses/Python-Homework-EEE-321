"""
03.10.2020
Boran Erhan 190403051

LIBRARY FOR SORTING ALGORITHMS

"""



from timeit import default_timer as timer


def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            end_index = midpoint - 1

        else:
            begin_index = midpoint + 1

    return None







def insertion(insert):
    for i in range(1, len(insert)):

        reference = insert[i]

        j = i - 1
        while j >= 0 and reference < insert[j]:
            insert[j + 1] = insert[j]
            j -= 1
        insert[j + 1] = reference


def mergesort(mylist):
    if len(mylist) > 1:
        mid = len(mylist) // 2
        left = mylist[:mid]
        right = mylist[mid:]

        insertion(left)
        insertion(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                mylist[k] = left[i]

                i += 1  # Move the index forward
            else:
                mylist[k] = right[j]
                j += 1

            k += 1  # Move to the next slot

        while i < len(left):
            mylist[k] = left[i]
            i += 1
            k += 1  # For the other values that stays in the lists.

        while j < len(right):
            mylist[k] = right[j]
            j += 1
            k += 1


def insertion_sort(list1):
    for i in range(1, len(list1)):  # For loop for Key index.

        key = list1[i]  # Key index for swapping.

        j = i - 1  # Comparison index for Key index.
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1  # Comparison algorithm
        list1[j + 1] = key
    return list1


def bubble(bubbles):
    for i in range(len(bubbles)):

        for j in range(1, len(bubbles) - i):

            if bubbles[j - 1] > bubbles[j]:  # necessary condition
                bubbles[j - 1], bubbles[j] = bubbles[j], bubbles[j - 1]  # for changing the indexes


