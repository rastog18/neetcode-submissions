# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(-1, None)
        itr = dummy

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        while(heap):
            val, idx, nodeToAdd, = heapq.heappop(heap)
            itr.next = nodeToAdd
            itr = itr.next
            if nodeToAdd.next:
                heapq.heappush(heap,(nodeToAdd.next.val, idx, nodeToAdd.next))
        return dummy.next

        """dummy = ListNode(-1, None)
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
            
            

        return dummy.next"""

        