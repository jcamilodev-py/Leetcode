from typing import Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        current = head

        while current:
            self.arr.append(current.val)
            current = current.next

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

s = Solution(l)
print(s.getRandom())