from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        dummy = ListNode(0)
        current = dummy

        while l1 != None and l2 != None:
            if l1.val > l2.val:
                current.next = l2
                current = current.next
                l2 = l2.next
            else:
                current.next = l1
                current = current.next
                l1 = l1.next
            
        if l1 != None:
            current.next = l1
            current = current.next
        elif l2 != None:
            current.next = l2
            current = current.next
        
        return dummy.next
        
        
    

s = Solution()
list1 = ListNode(4)
list1.next = ListNode(2)
list1.next.next = ListNode(1)
list1.next.next.next = ListNode(3)
print(s.sortList(list1))