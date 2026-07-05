# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1, None)
        itr = dummy

        if lists == []:
            return None

        while (True):
            NoneCtr = 0
            minNode = ListNode(1001, None)
            minIndx = -1
            print()
            for i, j in enumerate(lists):
                if j:
                    print(j.val)
                if j and (j.val < minNode.val):
                    minNode = j
                    minIndx = i
                
                if j == None:
                    print("incr")
                    NoneCtr += 1
            if NoneCtr == len(lists):
                break
                
            lists[minIndx] = minNode.next
            minNode.next = None
            itr.next = minNode
            itr = itr.next
            
            

        return dummy.next

        