class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hint: Which characters would you replace in a string to make all 
        #       its characters unique? Can you think with respect to the frequency 
        #       of the characters? - I would replace the charecters which are
        #       not the MOST frequent.

        l = 0
        maxC = 0
        hMap = {}
        for r in range(len(s)):
            hMap[s[r]] = 1 + hMap.get(s[r], 0)
            isValid = (r-l+1) - max(hMap.values()) <= k

            while(not isValid):
                maxC = max(maxC, r-l)
                hMap[s[l]] -= 1
                l += 1
                isValid = (r-l+1) - max(hMap.values()) <= k
    
        return max(maxC, r-l+1)
                
        