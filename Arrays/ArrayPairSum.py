# Defining the function for Array pair sum
# we try to keep the complexity at O(n)

def ArrayPairSum(array, sum):

    # checking the edge case
    if len(array)<2:
        return 'Length not sufficient'
    # we use set data structure for tracking the elements of the array
    seen = set()
    output = set()
    # Scanning through the array to check the number visited and the number we are targeting
    for num in array:
        target = sum - num
        # put the number you have visited in the array into seen set, don't put target
        if target not in seen:
            seen.add(num)
        else:
            # add the 2 numbers as a set inside the set
            output.add((min(num,target),max(num,target)))

    # mapping the string and the contents of the list / set output
    return ('\n'.join(map(str,list(output))))

print(ArrayPairSum([1,3,5,6,3], 6))
