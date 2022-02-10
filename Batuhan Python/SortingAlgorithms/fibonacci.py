def fibonacci(place):
    firstNumber = 1
    secondNumber = 1
    i = 2
    list=[1,1]


    while(i<place):
        firstNumber,secondNumber = secondNumber,(firstNumber+secondNumber)
        list.append(secondNumber)
        i+=1
    return list