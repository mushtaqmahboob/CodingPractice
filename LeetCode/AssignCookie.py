
class Solution:

    def assigncookie(self, g, s):

        g = sorted(g)
        s = sorted(s)

        contentchildren = 0

        i = len(g)-1
        j = len(s)-1

        while i>=0 and j>=0:
            if s[j] >= g[i]:

                contentchildren +=1
                i-=1
                j-=1
            else:
                i-=1

        return contentchildren

if __name__ == '__main__':
    greed = [1,2]
    size = [1,2,3]
    S = Solution()
    print(S.assigncookie(greed,size))

    greed2 = [1, 2, 3]
    size2 = [1, 1]
    print(S.assigncookie(greed2,size2))

'''
time complexity would be calculated for the sorting part in the beginning
in python sort() and sorted() methods are Tim Sort which is based on insertion sort and merge sort
so the worst time complexity would be O(N logN)

Space complexity would be constant because we only use a couple of variables but no data structure

'''
