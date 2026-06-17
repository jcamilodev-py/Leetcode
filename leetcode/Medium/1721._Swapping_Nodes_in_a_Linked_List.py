from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = 1


        while current != None:
            if count == k:
                left = current.val

            current = current.next
            count+=1
        
        current = head
        l = count - k 
        count = 1

        while current != None:
            if count == l:
                right = current.val
                current.val = left

            current = current.next
            count+=1
        
        current = head
        count = 1

        while current != None:
            if count == k:
                current.val = right
                return head.val
            
            current = current.next
            count+=1



s = Solution()
list1 = ListNode(1)

print(s.swapNodes(list1, 1))