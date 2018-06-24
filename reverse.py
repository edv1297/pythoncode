def stringReverse(inputString):
    if n == "": #BASE CASE: Empty String
        return n
    else:
        return (stringReverse(n[1:]) + n[0]) #Iterate and add the first character to the end...
