# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        itr = head
        while(itr):
            if (itr.val) == 2000:
                return True
            itr.val = 2000
            itr = itr.next
        return False
        