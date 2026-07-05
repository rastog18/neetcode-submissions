# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node1, node2) -> bool:
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        l = self.helper(node1.left, node2.left)
        r = self.helper(node1.right, node2.right)

        if l and r:
            return node1.val == node2.val
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        toRet = self.helper(p, q)
        return toRet
        

        