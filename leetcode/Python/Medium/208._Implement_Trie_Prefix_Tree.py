class Trie:

    def __init__(self):
        self.seen = set()
        self.pre = set()
        
    def insert(self, word: str) -> None:
        for i in range(len(word)):
            self.pre.add(word[:i+1])        

        self.seen.add(word)

    def search(self, word: str) -> bool:
        return word in self.seen
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.pre


o = Trie()
print(o.insert("apple"))
print(o.search("apple"))
print(o.search("app"))
print(o.startsWith("app"))
print(o.insert("app"))
print(o.search("app"))

