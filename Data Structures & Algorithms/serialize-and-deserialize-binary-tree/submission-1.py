# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        toRet = ""
        if root is None:
            return toRet
    
        stack = deque([])
        stack.append(root)

        while(stack):
            for i in range(len(stack)):
                node = stack.popleft()
                if node:
                    toRet += str(node.val) + ","
                    stack.append(node.left)
                    stack.append(node.right)
                else:
                    toRet += "null,"
        print(toRet)
        return toRet
            
                

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        stack = deque(data.split(","))
        temp = deque([])
        head = TreeNode(int(stack.popleft()))
        temp.append(head)
        while(temp):
            for i in range(len(temp)):
                node = temp.popleft()

                l_str = stack.popleft()
                if l_str != "null":
                    l = TreeNode(int(l_str))
                    node.left = l
                    temp.append(l)

                r_str = stack.popleft()
                if r_str != "null":
                    r = TreeNode(int(r_str))
                    node.right = r
                    temp.append(r)

        return head
            


