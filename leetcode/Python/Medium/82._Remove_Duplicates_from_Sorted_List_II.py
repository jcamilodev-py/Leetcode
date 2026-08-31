from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return 

        dummy = ListNode(0)
        c = dummy
        dummy.next = head
        prev = head
        current = head.next


        while current:
            if prev.val == current.val:
                prev = prev.next
                current = current.next
                dummy.next = current

            else:
                if dummy.next != prev.next:
                    dummy = dummy.next
                prev = prev.next
                current = current.next

        return c.next

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)
l.next.next.next.next.next = ListNode(4)
l.next.next.next.next.next.next = ListNode(5)

s = Solution()
print(s.deleteDuplicates(l))
