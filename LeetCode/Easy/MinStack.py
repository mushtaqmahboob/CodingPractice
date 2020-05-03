class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[:-1]

    def getMin(self) -> int:
        return min(self.items)

    def printstack(self):
        output = []
        rev = reversed(self.items)
        for ele in rev:
            output.append(ele)
        return '\n'.join(map(str, list(output)))


s = MinStack()
s.push(2)
s.push(3)
s.push(0)
print('result after pushing')
print(s.printstack())
s.pop()
print('Result after popping\n')

print(s.printstack())
print('min number in the stack')
print(s.getMin())
