'''
run a pointer 'i' from the beginning and another one 'j' from the end
when any alphabet is encountered we swap the values
when anything other than alphabet is encountered we ignore that and increment i pointer or decrement j
depending on where it occurred

'''

class Solution:

    def reverseOnlyLetters(self, s) -> str:

        i = 0
        j = len(s)-1

        str2=''
        chararray = list(s)

        while i<j:
            while i<j and not(str(chararray[i]).isalpha()):
                i+=1
            while i<j and not(str(chararray[j]).isalpha()):
                j-=1

            temp = chararray[i]
            chararray[i] = chararray[j]
            i+=1
            chararray[j] = temp
            j-=1

        return (str2.join(chararray))

if __name__=='__main__':
    string = "ab-cd"
    string2 = "a-bC-dEf-ghIj"
    string3 = "Test1ng-Leet=code-Q!"
    S = Solution()

    print(S.reverseOnlyLetters(string))

    print(S.reverseOnlyLetters(string2))

    print(S.reverseOnlyLetters(string3))

'''
Time complexity will be O(N), N = no.of characters in the string
Do not panic by seeing those 3 while loops, only one while loop is really iterating through
the other two are just incrementing or decrementing pointers.

Space complexity will be O(N)
as we take the string and convert it into character array so we use only an array by iterating through 
each character .

'''