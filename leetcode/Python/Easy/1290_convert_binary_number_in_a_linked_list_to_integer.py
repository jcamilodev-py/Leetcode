from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        result = 0

        while current:
            result = result * 2 + current.val
            current = current.next

        return result



    
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

s = Solution()
print(s.getDecimalValue(head))

        




