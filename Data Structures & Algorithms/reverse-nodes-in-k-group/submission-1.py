# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def recursiveHelper():
            # print("Called")
            prev = slow
            cur = slow.next
            start = slow.next
            while(cur != fast):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            start.next = cur
            slow.next = prev
                

        # keep a track of slow and fast pointers
        dummy = ListNode(-1, head)
        slow = dummy
        fast = dummy
        prev = dummy

        canChange = True
        for i in range(k):
            if fast:
                fast = fast.next
            else:
                canChange = False
        if canChange:
            fast = fast.next
            while(canChange):
                recursiveHelper()
                for i in range(k):
                    if fast:
                        fast = fast.next
                        slow = slow.next
                    else:
                        canChange = False
        return dummy.next
        # when the fast pointer 
        """toStore = node
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
        return dummy.next"""
        