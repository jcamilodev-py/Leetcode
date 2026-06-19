from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current = head
        n = 0
        nums = []
        while current:
            nums.append(current.val)
            n+=1
            current = current.next

        monotick = [0] * n
        stack = []
        current = head
        count = 0
        while current:
            while stack and current.val > nums[stack[-1]]:
                idx = stack.pop()
                monotick[idx] = current.val

            stack.append(count)
            current = current.next
            count+=1

        return monotick





s = Solution()
list1 = ListNode(2)
list1.next = ListNode(7)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(5)




print(s.nextLargerNodes(list1))