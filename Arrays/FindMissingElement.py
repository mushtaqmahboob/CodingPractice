
def findmissing(array1,array2):

    # using XOR, best for finding only 1 missing value

    result = 0
    for num in array1+array2:
        result ^=num
    return result



print(findmissing([1,2,3,4,5],[4,5,2,3]))

