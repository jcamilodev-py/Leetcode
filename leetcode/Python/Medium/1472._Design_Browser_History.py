class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next



class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.l = DoublyListNode(homepage)
        self.current = self.l
        

    def visit(self, url: str) -> None:
        n2 = DoublyListNode(url)
        self.current.next = n2
        n2.prev = self.current

        self.current = self.current.next
        
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev:
            self.current = self.current.prev
            steps-=1

        return self.current.val
               
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps-=1

        return self.current.val
        

o = BrowserHistory("leetcode.com")
print(o.visit("google.com"))
print(o.visit("facebook.com"))
print(o.visit("youtube.com"))
print(o.back(1))
print(o.back(1))
print(o.forward(1))
print(o.visit("linkedin"))
print(o.forward(2))
print(o.back(2))
print(o.back(7))



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)