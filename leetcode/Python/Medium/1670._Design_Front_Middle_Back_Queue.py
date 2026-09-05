class DoublyLinkedList:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class FrontMiddleBackQueue:

    def __init__(self):
        self.l = DoublyLinkedList(0)
        self.end = self.l
        self.slow = self.l
        self.fast = self.l

    def pushFront(self, val: int) -> None:
        reference = self.l.next
        self.l.next = DoublyLinkedList(val)
        self.l.next.next = reference
        if reference:
            reference.prev = self.l.next
        else:
            self.end = self.end.next

        self.l.next.prev = self.l


    def searchMiddle(self, slow, fast) ->DoublyLinkedList:
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def searchMiddleForPop(self, slow, fast):
        while fast.next and fast.next.next and fast.next.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def pushMiddle(self, val: int) -> None:
        if not self.l.next:
            return self.pushFront(val)

        slow = self.searchMiddle(self.l, self.l)
        
        reference = slow.next
        slow.next = DoublyLinkedList(val)
        slow.next.prev = slow
        slow.next.next = reference

        slow.next.next.prev = slow.next


    def pushBack(self, val: int) -> None:
        if not self.l.next:
            return self.pushFront(val)

        self.end.next = DoublyLinkedList(val)
        self.end.next.prev = self.end
        self.end = self.end.next


    def popFront(self) -> int:
        if self.l.next:
            v = self.l.next.val
            self.l.next = self.l.next.next

            if self.l.next:
                self.l.next.prev = self.l
            else:
                self.end = self.l
            return v
        return -1



    def popMiddle(self) -> int:
        if not self.l.next:
            return -1

        slow = self.searchMiddleForPop(self.l, self.l)

        v = slow.next.val
        d = slow.next

        slow.next = d.next
        if d.next:
            d.next.prev = slow
        else:
            self.end = slow

        return v


    def popBack(self) -> int:
        if not self.l.next:
            return -1

        v = self.end.val
        self.end = self.end.prev
        self.end.next = None

        return v

o = FrontMiddleBackQueue()

print(o.pushFront(3))
print(o.pushFront(2))
print(o.pushFront(1))
print(o.popFront())

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()