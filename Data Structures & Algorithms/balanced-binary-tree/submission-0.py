# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.status = True

    def helper(self, root: Optional[TreeNode]) -> int:
        if not self.status:
            return 0

        if root is None:
            return 0
        l = 1 + self.helper(root.left)
        r = 1 + self.helper(root.right)
        self.status = self.status and (abs(l-r) <= 1)
        return max(l, r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.status
        

        