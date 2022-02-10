"""
Batuhan Beel
180403031
28/09/2021

"""
def insertionSort(_list):

    for i in range(1, len(_list)):

        key= _list[i]
        j = i - 1

        while (j >= 0 and key < _list[j]):
            _list[j + 1] = _list[j]
            j -= 1
        _list[j + 1] = key
    return _list



