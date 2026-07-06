class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Hint: Which characters would you replace in a string to make all 
        #       its characters unique? Can you think with respect to the frequency 
        #       of the characters? - I would replace the charecters which are
        #       not the MOST frequent.

        l = 0
        count = {} # char -> count
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1 - maxf > k):
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
        return res
                
        