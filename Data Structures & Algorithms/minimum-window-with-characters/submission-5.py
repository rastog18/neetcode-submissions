class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s) < len(t)):
            return ""

        needMap, haveMap = {}, {}
        for i in t:
            needMap[i] = 1 + needMap.get(i, 0)
            haveMap[i] = 0
        have, need = 0, len(needMap)
        
 
        l, r = 0, 0
        minRes = s
        toReturn = False
    
        for r in range(0, len(s)):
            c = s[r]
            if c in haveMap:
                haveMap[c] += 1
                if haveMap[c] == needMap[c]:
                    have += 1

            # move the left pointer forward
            while (have == need):
                toReturn = True
                if len(minRes) > (r-l+1):
                    minRes = s[l:r+1]
                c2 = s[l]
                if (c2 in haveMap):
                    haveMap[c2] -= 1
                    if (haveMap[c2] < needMap[c2]):
                        have -= 1
                l += 1

        
        if (toReturn == False):
            return ""
        return minRes
            
            



        