# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.val = -1
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #inorder traversal
        def inorderTraversal(node):
            if self.val > -1:
                return
            if node is None:
                return
            
            inorderTraversal(node.left)
            self.count += 1
            if self.count == k:
                self.val = node.val
            inorderTraversal(node.right)
    
        inorderTraversal(root)
        return self.val

        