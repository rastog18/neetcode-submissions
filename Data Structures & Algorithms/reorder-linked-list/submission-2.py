# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while (fast.next and fast.next.next):
            slow =  slow.next
            fast = fast.next.next
        
        prev = None
        head2 = slow.next
        itr = head2
        slow.next = None

        while(itr):
            store = itr.next
            itr.next = prev
            prev = itr
            itr = store

        itr = head
        itr2 = prev
        while(itr and itr2):
            store = itr.next
            store2 = itr2.next
            itr.next = itr2
            itr2.next = store

            itr = store
            itr2 = store2
        

            



                

        