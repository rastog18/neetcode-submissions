class trieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfString = False

class PrefixTree:

    def __init__(self):
        self.root = trieNode()

    def insert(self, word: str) -> None:
        word = word.upper()
        itr = self.root
        for ch in word:
            if itr.children[ord(ch)-65] == None:
                newNode = trieNode()
                itr.children[ord(ch)-65] = newNode
            itr = itr.children[ord(ch)-65]
            if word[-1] == ch:
                itr.isEndOfString = True

    def search(self, word: str) -> bool:
        word = word.upper()
        itr = self.root
        for ch in word:
            if itr.children[ord(ch)-65] == None:
                return False
            itr = itr.children[ord(ch)-65]
        if itr.isEndOfString:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        prefix = prefix.upper()
        itr = self.root
        for ch in prefix:
            if itr.children[ord(ch)-65] == None:
                return False
            itr = itr.children[ord(ch)-65]
        return True
        
        