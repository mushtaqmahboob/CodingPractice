
def findmissing(array1,array2):

    # using the set data structure
    seen = set()
    output = set()

    for ele in array1:
        if ele in array2:
            seen.add(ele)
        else:
            output.add(ele)

    return output

print(findmissing([1,2,3,4,5],[4,5,2,3]))