
def findmissing(array1,array2):

    # using dictionary
    count = {}
    output=set()

    for num in array1:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    for num in array2:
        if num in count:
            count[num]-=1
        else:
            count[num]=1
    for k in count:
        if count[k]!=0:
            output.add(k)
    return '\n'.join(map(str,list(output)))



print(findmissing([1,2,3,4,5],[4,5,2,3]))
print(findmissing([1,2,3,4,5,6,7,8,9],[4,5,2,3]))
