class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        
    def push(self, value: int) -> None:
        self.stack.append(value)
        self.minimum = min(self.minimum, value)
        
    def pop(self) -> None:
        d = self.stack.pop()
        if d == self.minimum:
            if self.stack:
                self.minimum = min(self.stack)
            else:
                self.minimum = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
o = MinStack()
print(o.push(2147483646))
print(o.push(2147483646))
print(o.push(2147483647))
print(o.top())
print(o.pop())
print(o.getMin())
print(o.pop())
print(o.getMin())
print(o.pop())
print(o.push(2147483647))
print(o.top())
print(o.getMin())
print(o.push(-2147483648))
print(o.top())
print(o.getMin())
