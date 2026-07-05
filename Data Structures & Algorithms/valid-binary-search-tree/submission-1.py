# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.toRet = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node) -> List[int]:
            if node is None:
                return

            l = helper(node.left)
            r = helper(node.right)
            if l and r:
                if not (l[1] < node.val and node.val < r[0]):
                    self.toRet = False
                return [l[0], r[1]]
            elif r:
                if not (node.val < r[0]):
                    self.toRet = False
                return [node.val, r[1]]
            elif l:
                if not (l[1] < node.val):
                    self.toRet = False
                return [l[0], node.val]
        
            return [node.val, node.val]

        helper(root)
        return self.toRet

        