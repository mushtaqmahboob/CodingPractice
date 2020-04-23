'''
We first take the array/list as the parameter
Initialize i to zero to track the array and index to zero to return the size of the array/list
run a while loop to iterate through with 'i'
run another while loop to iterate using 'j' to check the occurrence of the current element and check if the elements are still same
keep on incrementing the 'j' loop until we find a different element other than the previous one

immediately record that element in char array itself using the 'index' variable
and check if j-i >1 because the 2nd example is this constraint and we should not do any changes in array if j-i<=1
take variable 'count' and store the j-i value as a string because we need to iterate through it and store the values individually
in the array.
Now shift the i pointer in the place of j using i=j
exit from the while loop and return the index value
'''

def compress(chars) -> int:

    i=0
    index=0

    while i<len(chars):
        j=i
        while j<len(chars) and chars[j]==chars[i]:
            j+=1

        chars[index] = chars[i]
        index+=1
        if j-i>1:
            count = str(j-1)
            for c in count:
                chars[index]=c
                index+=1
        i=j
    return index


# Test code

listt=["a","a","b","b","c","c","c"]
print(compress(listt))

'''
The time complexity would be O(n) where n= no.of characters
Space complexity is O(1) because we didn't use any data structure
but few variables that's it so i should be fine.
'''