class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            
        # create an adjCencyList if both of them are equal return true
        sAdjList = {}
        for char in s:
            sAdjList[char] = sAdjList.get(char, 0) + 1

        tAdjList = {}
        for char in t:
            tAdjList[char] = tAdjList.get(char, 0) + 1

        if tAdjList == sAdjList:
            return True
            
        return False
        