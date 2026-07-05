
class Node:
    def __init__(self, current: str, openBrace: int, closeBrace: int):
        self.current = current
        self.openBrace = openBrace
        self.closeBrace = closeBrace
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.output = []

    def buildTree(self, node: Node):
        if node.closeBrace == 0:
            self.output.append(node.current)
            return

        if (node.openBrace > 0):
            node.left = Node(node.current + "(", node.openBrace-1, node.closeBrace)
            self.buildTree(node.left)

        if (node.openBrace < node.closeBrace):
            node.right = Node(node.current + ")", node.openBrace, node.closeBrace-1)
            self.buildTree(node.right)

        
        
    def generateParenthesis(self, n: int) -> List[str]:
        root = Node("(", n-1, n)
        self.buildTree(root)
        print(self.output)
        return self.output
            
            


        