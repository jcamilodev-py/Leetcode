from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        current_dummy = dummy
        current = ListNode(0)
        current.next = head
        ans = current

        while current.next:

            if current.next.val >= x:
                current_dummy.next = ListNode(current.next.val)
                current_dummy = current_dummy.next

                current.next = current.next.next 
            else:
                current = current.next

        current.next = dummy.next
        
        return ans.next
        
            




l = ListNode(2)
l.next = ListNode(1)




s = Solution()
print(s.partition(l, 2))