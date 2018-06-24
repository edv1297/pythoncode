def reverse(input):
    return splitString(input)



def splitString(someString):
    if len(someString) <=1:
        return someString
    else:
        half1, half2 = someString[:len(someString)//2], someString[len(someString)//2:]
        return splitString(half1), splitString(half2)


print reverse("apple")
