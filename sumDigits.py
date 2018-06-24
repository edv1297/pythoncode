def digitSum(inputString):
    if len(str(inputString))==1: #When ther are no more digits to add, return the answer
        return inputString
    else:
        return digitSum(inputString/10) + (inputString%10) # divide by 10, removes the last digit and modular division by 10 keeps everything except the last
