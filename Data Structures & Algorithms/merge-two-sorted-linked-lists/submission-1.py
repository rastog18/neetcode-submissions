# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def addItem(ptr):
            nonlocal newH, newArray
            if newH is None:
                newH = ptr
                newArray = ptr
            else:
                newArray.next = ptr
                newArray = newArray.next
    
        newArray = None
        newH = None
        p1 = list1
        p2 = list2
        while(p1 or p2):
            if p1 and p2:

                if p1.val < p2.val:
                    addItem(p1)
                    p1 = p1.next
                else:
                    addItem(p2)
                    p2 = p2.next
            elif p1:

                addItem(p1)
                p1 = p1.next
            else:

                addItem(p2)
                p2 = p2.next
        return newH

        """l1 = list1
        l2 = list2
        toReturn = None
        toReturnH = None

        while(l1 and l2):
            toPut = None
            if l1.val < l2.val:
                toPut = l1
                l1 = l1.next
            else:
                toPut = l2
                l2 = l2.next
    
            if toReturnH == None:
                toReturn = toPut
                toReturnH = toPut
            else:
                toReturn.next = toPut
                toReturn = toReturn.next
        if l1:
            if toReturnH == None:
                return l1
            toReturn.next = l1
        if l2:
            if toReturnH == None:
                return l2
            toReturn.next = l2
        return toReturnH"""
            


        