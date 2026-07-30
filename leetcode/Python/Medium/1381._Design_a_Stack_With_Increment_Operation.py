class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.lenn = 0

    def push(self, x: int) -> None:
        if self.lenn < self.maxSize:
            self.stack.append(x)
            self.lenn+=1

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        self.lenn-=1
        return self.stack.pop()
    

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.lenn)):
            self.stack[i]+=val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)