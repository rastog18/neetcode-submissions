# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find a mid point
            # two pointer approcah to reverse the array after that
        #reverse the list after the mid point
        #join the arrays
        slow = head
        fast = head

        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next


        cur = slow.next
        slow.next = None
        prev = None

        while (cur):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp


        l1 = head
        l2 = prev
            
        while(l1 and l2):
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2

        

        
        """
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
            itr2 = store2"""