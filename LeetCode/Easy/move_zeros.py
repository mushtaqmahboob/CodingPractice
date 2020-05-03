

def movingzero(array):

    if len(array) == 0:
        return 'Array size not sufficient'

    pos = 0

    for i in range(len(array)):
        if array[i] != 0:
            array[pos], array[i] = array[i], array[pos]
            pos+=1


    return array

print(movingzero([0,1,0,3,12]))

'''
time complexity would be O(N)
space complexity would be constant because its inplace exchange of elements
'''