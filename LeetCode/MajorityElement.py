

def majority(array):

    result = (len(array)//2)
    if len(array) == 0:
        return 'Empty Array'

    counter = {}

    for ele in array:
        if ele in counter:
            counter[ele]+=1
        elif ele not in counter:
            counter[ele] = 1

    for k in counter:
        if counter[k] > result:
            return k

print(majority([3,2,3]))

'''
time complexity O(n)
space is also O(n)
'''