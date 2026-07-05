"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.root = None
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        adjList = {}
        visited = set()

        def bt(copy, itr):
            # print(itr .val)
            if copy in visited:
                # print("return")
                return
            # print("here")
            # print(adjList, end = " ")
            
            visited.add(copy)
            # print(itr.neighbors)
            for neighbor in itr.neighbors:
                print(neighbor.val)
                newNode = adjList.get(neighbor.val)
                if  newNode is None:
                    # create node
                    # print("node creation")
                    newNode = Node(neighbor.val)
                    adjList[newNode.val] = newNode

                # create a connection
                if copy.val < neighbor.val:
                    copy.neighbors.append(newNode)
                    newNode.neighbors.append(copy)
                if newNode not in visited:
                    bt(newNode, neighbor)
                
        itr = node
        self.root = Node(itr.val)
        adjList[self.root.val] = self.root
        bt(self.root, itr) 
        return self.root