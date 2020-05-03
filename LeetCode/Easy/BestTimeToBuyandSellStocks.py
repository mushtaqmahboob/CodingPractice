

def besttime(array):

    profit = 0

    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            profit = profit + (array[i+1]-array[i])
        else:
            pass

    return profit

print(besttime([7,1,5,3,6,4]))

'''
time complexity : O(n)
space complexity : O(1)
'''