"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def recursiveCreateNode(itr):
            if itr == None:
                return None
            newNode = Node(itr.val, None, None)
            adjList[itr] = newNode
            newNode.next = recursiveCreateNode(itr.next)
            return newNode
        #create a deep copy of linkedList with random pointer = null
        itr = head
        adjList = {} #oldListNode -> newListNode
        dummy = recursiveCreateNode(itr)

        #set random pointer
        itr = head
        itr2 = dummy
        while(itr):
            itr2.random = adjList.get(itr.random, None)
            
            itr = itr.next
            itr2 = itr2.next
        return dummy
        """l1Adj = {}
        l2Adj = {}

        itr = head
        head2 = None
        prev = None

        lList = 0
        while(itr):
            # add the address : index to the Adjacency List
            l1Adj[itr] = lList

            # for the newList create a node
            newNode = Node(itr.val, None, None)
            l2Adj[lList] = newNode
            if prev == None:
                head2 = newNode
            else:
                prev.next = newNode

            #increment to next ptr
            prev = newNode
            itr = itr.next
            lList += 1
        
        
        itr = head
        prev = head2
        while(itr):
            if itr.random:
                prev.random = l2Adj[l1Adj[itr.random]]
            
            itr = itr.next
            prev = prev.next
        
        return head2"""
        