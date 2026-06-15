import random
class RandomizedSet:

    def __init__(self):
        self.seen = set()
        self.idx = 0
        

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        else:
            self.seen.add(val)
            return True
         

    def remove(self, val: int) -> bool:
        if val in self.seen:
            self.seen.remove(val)
            return True
            
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.seen))
        


obj = RandomizedSet()
print(obj.remove(0))
print(obj.remove(0))
print(obj.insert(0))
print(obj.insert(1))

print(obj.getRandom())



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()