def anagram(s1,s2):

    a1 = sorted(s1.replace(' ','').lower())
    a2 = sorted(s1.replace(' ','').lower())

    return a1 == a2

print(anagram('akram','akmra'))

