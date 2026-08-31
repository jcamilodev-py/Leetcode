class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.n = 0
        self.l = ListNode()
        self.current = self.l
        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            value = ListNode(value)
            self.current.next = value
            self.current = self.current.next
            self.n+=1
            return True

        return False

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.l.next.next:
            self.l.next = self.l.next.next
        else:
            self.l.next = None
        self.n-=1
        if self.isEmpty():
            self.current = self.l

        return True
        

    def Front(self) -> int:
        return self.l.next.val if self.n > 0 else -1
        

    def Rear(self) -> int:
        return self.current.val if self.n > 0 else -1
        

    def isEmpty(self) -> bool:
        return True if self.n == 0 else False
        
        

    def isFull(self) -> bool:
        return True if self.n == self.k else False
        

o = MyCircularQueue(6)

print(o.enQueue(6))
print(o.Rear())
print(o.enQueue(3))

print(o.Front())
print(o.Rear())

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()