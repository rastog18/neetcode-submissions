# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.numGoodNodes = 0
    def goodNodes(self, root: TreeNode) -> int:
        maxNode_val = -101

        def helper(node, maxNode_val):
            if node is None:
                return
            temp = maxNode_val
            if node.val >= maxNode_val:
                self.numGoodNodes += 1
                temp = node.val
            helper(node.left, temp)
            helper(node.right, temp)
        
        helper(root, maxNode_val)
        return self.numGoodNodes

        