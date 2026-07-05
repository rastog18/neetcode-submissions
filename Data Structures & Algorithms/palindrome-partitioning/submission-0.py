class Solution:
    def ifPalindrome(self,s):
        if s == "":
            return False
    
        l = 0
        r = len(s)-1
        while(l <= r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        toRet = []
        substring = [""]
        def bt(i):
            # print("entering with", end="")
            # print(i)
            if i >= len(s):
                # print("need to skip this")
                # if last element of substring is a palindrome add
                if self.ifPalindrome(substring[-1]):
                    toRet.append(substring.copy())
                return
            if self.ifPalindrome(substring[-1]):
            # if a palindrome:
                # consider as palindrom
                # substring[-1] += s[i]
                # bt(i+1)
                # substring[-1] -= s[i]
                # do not consider as palindrome
                substring.append(s[i])
                bt(i+1)
                substring.pop()
            # else:
                # add to substring
                # consider a palindrome
            # print("using i = ", end = "")
            # print(i)
            substring[-1] += s[i]
            bt(i+1)
            # substring.pop()
        bt(0)
        return toRet