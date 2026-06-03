class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        

    def get(self, key: int) -> int:
        if key in self.dic.keys():
            k = self.dic[key]
            del self.dic[key]
            self.dic[key] = k
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            del self.dic[key]
            self.dic[key] = value
        else:
            if len(self.dic) == self.capacity:
                for i in self.dic:
                    del self.dic[i]
                    self.dic[key] = value
                    break
            else:
                self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param1 = obj.get(2)
obj.put(2,6)
param2 = obj.get(1)
obj.put(1,5)
obj.put(1,2)
param3 = obj.get(1)
param4 = obj.get(2)

# output [null, -1, null, -1, null, null, 2, 6]
print(param1, param2, param3, param4)

        
