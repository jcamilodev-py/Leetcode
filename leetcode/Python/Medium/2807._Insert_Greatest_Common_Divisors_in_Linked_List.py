from typing import Optional
from math import gcd

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        current = head.next

        ans = ListNode(head.val)
        current_ans = ans 

        while current:
            current_ans.next = ListNode(gcd(prev.val, current.val))
            current_ans.next.next = ListNode(current.val)
            current_ans = current_ans.next.next

            prev = prev.next
            current = current.next
        
        return ans


l = ListNode(18)
l.next = ListNode(6)
l.next.next = ListNode(10)
l.next.next.next = ListNode(3)

s = Solution()
print(s.insertGreatestCommonDivisors(l))