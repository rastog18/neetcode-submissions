# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, node1, node2) -> bool:
        if (node1 is None) and (node2 is None):
            return True
        if (node1 is None) or (node2 is None):
            # if node1:
                # print("node val:" + str(node1.val))
            return False
        # print("helper at" + str(node1.val))
        l = self.helper(node1.left, node2.left)
        r = self.helper(node1.right, node2.right)
        if l and r and node1.val == node2.val:
            return True
        else:
            return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        # print("Seaching for " + str(root.val))
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        if root.val == subRoot.val:
            return self.helper(root, subRoot) or l or r
        return l or r
        
        