def sumEven(input):
    if (input == 0):
        return 0;
    elif (input%2 ==0): #even number
        return input + sumEven(input-2)
    else:
        return sumEven(input-1)
