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
            if not self.toRet:
                return [math.inf, -math.inf] # exit early
                
            if node is None:
                return [math.inf, -math.inf]

            l = helper(node.left)
            r = helper(node.right)
            if node.left:
                if l[1] >= node.val:
                    self.toRet = False
            if node.right:
                if node.val >= r[0]:
                    self.toRet = False
            lMin = min(l[0], node.val)
            rMax = max(r[1], node.val)
            return [lMin, rMax]
            
        helper(root)
        return self.toRet

        