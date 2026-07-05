"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {} # mapping from old node to cloned node
        def clone(node):
            if node is None:
                return None
            if node in oldToNew:
                    return oldToNew[node]
            newNode = Node(node.val)
            oldToNew[node] = newNode
            for nNode in node.neighbors:
                toAppend = clone(nNode)
                newNode.neighbors.append(toAppend)
            return newNode

        return clone(node)