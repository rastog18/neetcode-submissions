# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lList = 1

        itr = head # len(nums)
        while(itr):
            lList += 1
            itr = itr.next
        
        prev = None
        itr = head
        lEnd = None
        mid = (lList // 2) - 1
        i = 0
        while(itr):
            if i > mid:
                store = itr.next
                itr.next = prev
                prev = itr
                itr = store
                
            else:
                lEnd = itr
                i += 1
                itr = itr.next
        lEnd.next = None
    
        itr = head
        itr2 = prev
        while(itr and itr2):
            store = itr.next
            store2 = itr2.next
            itr.next = itr2
            itr2.next = store
            if store == None:
                itr2.next = store2

            itr = store
            itr2 = store2
        

            



                

        