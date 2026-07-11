from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        leen, tail = 1, head

        while tail.next:
            tail = tail.next
            leen+=1

        k = k%leen
        if k == 0:
            return head
        
        current = head

        for i in range(leen - k - 1):
            current = current.next
        
        ans = current.next
        current.next = None
        tail.next = head

        return ans

    
        
s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

print(s.rotateRight(l, 2))