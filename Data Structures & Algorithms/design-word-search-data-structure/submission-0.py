class trieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfString = False

class WordDictionary:
    def __init__(self):
        self.root = trieNode()        

    def addWord(self, word: str) -> None:
        word = word.upper()
        itr = self.root

        for i,ch in enumerate(word):
            if itr.children[ord(ch) - 65] is None:
                newNode = trieNode()
                itr.children[ord(ch) - 65] = newNode
            itr = itr.children[ord(ch) - 65]
            if i == len(word)-1:
                itr.isEndOfString = True
        
    def search(self, word: str) -> bool:
        itr = self.root

        def bt(ichar, itr):
            if ichar >= len(word) and itr:
                return itr.isEndOfString
            if itr is None:
                return False

            char = word[ichar].upper()
            toRet = False
            if char == ".":
                for i in itr.children:
                    if i:
                        toRet = toRet or bt(ichar+1, i)
            else:
                if itr.children[ord(char) - 65]:
                    toRet = bt(ichar+1, itr.children[ord(char) - 65])
                else:
                    return False
            return toRet
        return bt(0, itr)
        
