from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        current2 = head
        n = 0
        ans = 0

        while current:
            n+=1
            current = current.next
        
        if n == 1:
            return 

        n = n // 2
        while current2:
            if ans == n-1:
                current2.next = current2.next.next
                break
            ans+=1
            current2 = current2.next

        return head
        

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(6)

s = Solution()
print(s.deleteMiddle(head))
