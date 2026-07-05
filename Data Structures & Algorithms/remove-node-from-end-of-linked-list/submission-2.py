# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove item at index = len(nums) - n 

        dummy = ListNode(0, head)
        
        # dummy -> 1 -> 2 -> 3 -> 4
        # slow -> dummy
        # fast -> 2

        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        
        # slow -> 2
        # fast -> 4
        while(fast.next):
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next
"""
        itr = head
        lList = 0
        while(itr):
            lList += 1
            itr = itr.next
        
        removeAt = lList - n
        itr = head
        i = 0
        print(removeAt)
        while(itr):
            if (i == removeAt - 1):
                if itr.next:
                    itr.next = itr.next.next
                return head
            elif removeAt == 0:
                return head.next

            i += 1
            itr = itr.next"""
        