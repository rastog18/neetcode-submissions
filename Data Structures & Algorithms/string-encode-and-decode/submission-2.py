class Solution:

    def encode(self, strs: List[str]) -> str:
        # append with a unique char - not UTF-8 char
        toRet = []
        for i in strs:
            toRet.append(str(len(i)))
            toRet.append("#")
            toRet.append(i)
        return "".join(toRet)

    def decode(self, s: str) -> List[str]:
        # split based on non UTF-8 char
        toRet = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            till = int(s[i:j])
            toRet.append(s[j+1:j+1+till])
            i = j+1+till
        return toRet
