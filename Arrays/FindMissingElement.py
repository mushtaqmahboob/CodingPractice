
def findmissing(array1,array2):

    # Sort the arrays and using the zip function of python
    array1.sort()
    array2.sort()

    for num1,num2 in zip(array1,array2):
        if num1 != num2:
            return num1

    return array1[-1]


print(findmissing([1,2,3,4,5],[4,5,2,3]))
print(findmissing([10,20,40,30,99],[20,10,30,40]))