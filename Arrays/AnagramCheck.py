def anagram(s1,s2):

    # initialising a dictionary to use
    count = {}

    # removing spaces and making it lower

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # edge case checking

    if len(s1) != len(s2):
        return False
    # Counting all the alphabet and storing the the count dictionary
    for letter in s1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1

    # Scan the 2nd array and remove letter from count which you encounter during the scan

    for letter in s2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1

    # Checking if any element is remaining in the dictionary. If no element is remaining then its an anagram
    # Checking is count has any non zero value
    for k in count:
        if count[k] !=0:
            return False

    return True


print(anagram('akram','akmra'))
print(anagram('mushtaq','mahboob'))
print(anagram('098776','123344'))
print(anagram('12345','54321'))


