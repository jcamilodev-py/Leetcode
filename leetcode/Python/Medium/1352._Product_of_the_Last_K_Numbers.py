class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]
        
    def add(self, num: int) -> None:
        if num == 0:self.pre = [1]
        else:self.pre.append(num * self.pre[-1])
        
    def getProduct(self, k: int) -> int:
        if k >= len(self.pre): return 0

        return self.pre[-1] // self.pre[-1 - k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
print(obj.add(4))
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))