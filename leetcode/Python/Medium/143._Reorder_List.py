from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next

        slow.next = None
        head1 = head

        prev = None
        current = head2

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        head2 = prev

        while head1 and head2:
            n = head1.next
            n2 = head2.next

            head1.next = head2
            head2.next = n

            head1, head2 = n, n2
        
        return head

            


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)

s = Solution()
print(s.reorderList(l))
