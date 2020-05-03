

def missing(nums):

    nums.sort()

    if len(nums) != nums[-1]:
        return len(nums)

    for i in range(len(nums)-1):
        expected = nums[i]+1
        if nums[i+1]!=expected:
            return expected


print(missing([3,0,1]))

'''
time complexity : O(nlogn) because we used .sort() a type of tim sort
space complexity : O(1) its all happening in place
'''