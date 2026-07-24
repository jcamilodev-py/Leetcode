from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if current.val in seen:
                prev.next = current.next
                current = current.next
            else:
                current = current.next
                prev = prev.next
            
        return dummy.next       

        

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

s = Solution()
print(s.modifiedList([1,2,3], l))