# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = None
        itr = head
        if itr == None:
            return itr
        while(itr.next):
            prev = cur
            cur = itr
            itr = itr.next

            cur.next = prev
        itr.next = cur
        return itr



        