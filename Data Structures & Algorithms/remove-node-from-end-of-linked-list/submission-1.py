# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove item at index = len(nums) - n 

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
            itr = itr.next
        