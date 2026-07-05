class Solution:
    def ifPalindrome(self,s):
        if s == s[::-1]:
            return True
        return False

    def partition(self, s: str) -> List[List[str]]:
        
        toRet = []
        substring = []

        def bt(start):
            if start >= len(s):
                toRet.append(substring.copy())
                return

            for end in range(start + 1, len(s)+1):
                if self.ifPalindrome(s[start:end]):
                    substring.append(s[start:end])
                    bt(end)
                    substring.pop()

        bt(0)
        return toRet