
class Solution:

    def veifyAlienDictionary(self, words, order) -> bool:

        records = []

        for i in range(len(words)-1):
            for j in range(min(len(words[i]),len(words[i+1]))):

                if words[i][j]==words[i+1][j]:
                    continue
                records.append([words[i][j],words[i+1][j]])
                break

        if records == []:
            return False
        for record in records:
            if order.index(record[0]) > order.index(record[1]):
                return False
        return True

if __name__ == '__main__':
    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    S= Solution()
    print(S.veifyAlienDictionary(words,order))

    words2 = ["hello", "leetcode"]
    order2 = "hlabcdefgijkmnopqrstuvwxyz"
    print(S.veifyAlienDictionary(words2,order2))

    words3=["ubg", "kwh"]
    order3="qcipyamwvdjtesbghlorufnkzx"
    print(S.veifyAlienDictionary(words3,order3))

    words4 = ["apple", "app"]
    order4 = "abcdefghijklmnopqrstuvwxyz"
    print(S.veifyAlienDictionary(words4,order4))


'''
The time complexity will be O(M*N), M = No.of words, N = no.of characters in the word
and the space complexity also O(M*N), but since the word's length constraint is always <=20
and the whole words list length is 100, it becomes constant time when worst case is considered.

'''

