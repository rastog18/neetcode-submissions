# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.stack = deque([])
        self.toRet = []
    
    def helper(self):
        temp = []
        temp_val = []
        while self.stack:
            node = self.stack.popleft()
            temp.append(node)
            temp_val.append(node.val)
        self.toRet.append(temp_val)
        for node in temp:
            if node.left:
                self.stack.append(node.left)
            if node.right:
                self.stack.append(node.right)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return self.toRet

        self.stack.append(root)
        while(self.stack):
            self.helper()
        return self.toRet


        