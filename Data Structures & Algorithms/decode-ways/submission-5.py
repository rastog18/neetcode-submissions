class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        OPT = [0] * n

        # Base Case
        if s[0] == "0":
            return 0
        OPT[0] = 1
        if n >= 2:
            if s[1] == "0":
                if s[0] <= "2":
                    OPT[1] = OPT[0]
                else:
                    return 0
            elif s[:2] <= "26":
                OPT[1] = 1 + OPT[0]
            else:
                OPT[1] = OPT[0]
        
        # Recuurance Relation
        for i in range(2, n):
            if s[i] == "0":
                if "0" < s[i-1] and s[i-1] <= "2":
                    OPT[i] = OPT[i-2]
                else:
                    return 0
            elif s[i-1:i+1] <= "26" and s[i-1] != "0":
                OPT[i] = OPT[i-2] + OPT[i-1]
            else:
                OPT[i] = OPT[i-1]

        return OPT[n-1]

        