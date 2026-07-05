# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.curMax = -1

    def helper(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.curMax = max(self.curMax, l+r)
        l += 1
        r += 1
        return max(l, r)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # maxDiameter for every node is the sum of its left and right depth
        self.helper(root)
        return self.curMax
        

        