# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        itr = head
        ITR = head.next
        while(itr and ITR):
            if (itr == ITR):
                return True
            itr = itr.next
            if (ITR.next):
                ITR = ITR.next.next
            else:
                return False
        return False
        