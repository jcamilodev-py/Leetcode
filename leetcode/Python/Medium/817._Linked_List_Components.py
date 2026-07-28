from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        seen = set(nums)
        current = head
        ans = 0
        f = True
        while current:
            if current.val not in seen:
                f = True
            elif f:
                f = False
                ans+=1

            current = current.next
        return ans




l = ListNode(0)
l.next = ListNode(1)
l.next.next = ListNode(2)
l.next.next.next = ListNode(3)
l.next.next.next.next = ListNode(4)

s = Solution()
print(s.numComponents(l, nums = [0,1,3]))