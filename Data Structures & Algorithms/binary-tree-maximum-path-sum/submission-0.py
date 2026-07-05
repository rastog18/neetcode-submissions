# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxPath = -1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def helper(node):
            if node is None:
                return 0 

            l = helper(node.left)
            r = helper(node.right)

            self.maxPath = max(self.maxPath, l+r+node.val, l+node.val, r+node.val, node.val)
            if max(l, r) > 0:
                return max(l,r) + node.val
            return node.val

        helper(root)
        return self.maxPath