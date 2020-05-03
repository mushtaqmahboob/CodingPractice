
def defangip(address: str) -> str:

    result = ''
    for element in address:
        if element=='.':
            result+='[.]'
        else:
            result+=element

    return result

'''
The time complexity would be O(n) where n is the no.of characters of the address
 but if you think, the ip addresses are almost a constant size, so the time will be same for every address
so this would become O(1) that is constant time
 
 The space complexity would be again O(n) where n is no.of characters of the address
 but again ip addresses are almost always same size so the space complexity would also be same size.
 
 But again if you want you can explain this to the interviewer.
 '''
# Test code
addr = '198.2.0.5'
print('The given input is '+addr)

print('The output is '+defangip(addr))

