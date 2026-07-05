class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        adjList = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        toRet = []
        subset = []
        if digits == "":
            return toRet

        def bt(i):
            if i >= len(digits):
                toAppend = ""
                for k in subset:
                    toAppend += k
                toRet.append(toAppend)
                return
    
            num = digits[i]
            for j in adjList[num]:
                subset.append(j)
                bt(i+1)
                subset.pop()
        
        bt(0)
        return toRet
        