class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.present = False
        self.isEndOfString = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def createTree(self, words):
        for word in words:
            itr = self.root
            for i, ch in enumerate(word):
                ch = ch.upper()
                if itr.children[ord(ch) - 65] is None:
                    newNode = TrieNode()
                    itr.children[ord(ch) - 65] = newNode
                itr = itr.children[ord(ch) - 65]
                if i == len(word)-1:
                    itr.isEndOfString = True
                    break
                
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.createTree(words)

        toRet = []
        subset = []
        visited = set()

        def bt(i, j, itr):
            # check if index is in trie and continue doing so
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return
            

            char = board[i][j].upper()
            if itr.children[ord(char) - 65]:
                next_itr = itr.children[ord(char) - 65]
                subset.append(board[i][j])
                visited.add((i,j))
                if next_itr.isEndOfString is True and next_itr.present is False:
                    next_itr.present = True
                    toRet.append("".join(subset))

                if (i+1, j) not in visited:
                    bt(i+1, j, next_itr)
                if (i-1, j) not in visited:
                    bt(i-1, j, next_itr)
                if (i, j+1) not in visited:
                    bt(i, j+1, next_itr)
                if (i, j-1) not in visited:
                    bt(i, j-1, next_itr)
                visited.remove((i,j))
                subset.pop()
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                itr = self.root
                bt(i, j, itr)

        return toRet
        