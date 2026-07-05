# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        toRet = []
        if root is None:
            return toRet
        queue = deque([])
        queue.append(root)
        
        while(queue):
            temp_val = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp_val.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            toRet.append(temp_val[-1])

        return toRet

        