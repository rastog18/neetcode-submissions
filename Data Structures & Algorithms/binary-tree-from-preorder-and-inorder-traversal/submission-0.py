# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Map value -> index in inorder traversal for O(1) lookup
        inorder_map = {value: idx for idx, value in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Pick the current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Split inorder around this value
            idx = inorder_map[root_val]

            # Build left and right subtrees
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)

            return root

        return helper(0, len(inorder) - 1)
    