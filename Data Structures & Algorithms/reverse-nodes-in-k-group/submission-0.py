# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseOneGroup(self, node, k):
        toStore = node
        toReturn = node.next
        node = node.next

        count = 1
        itr = node
        while(itr and itr.next and count<k):
            itr = itr.next
            count += 1
        
        if count == k:
            prev = itr.next
            itr = node
            while (itr and count > 0):
                count -= 1
                itrN = itr.next
                itr.next = prev

                prev = itr
                itr = itrN
            toStore.next = prev
            return toReturn
        return toStore

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
    
        dummy = ListNode(10,head)
        node = dummy
        while(True):
            node2 = self.reverseOneGroup(node, k)
            if (node2 == node):
                break
            node = node2
        return dummy.next
        