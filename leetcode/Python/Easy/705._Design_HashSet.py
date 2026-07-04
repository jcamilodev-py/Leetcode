class MyHashSet:

    def __init__(self):
        self.seen = set()
        

    def add(self, key: int) -> None:
        self.seen.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.seen:
            self.seen.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.seen:
            return True
        return False

obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))