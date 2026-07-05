class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        toRet = []

        def backtrack(temp, subset):
            if temp == []:
                toRet.append(subset.copy())
                return
            for i in range(len(temp)):
                subset.append(temp[i])
                backtrack(temp[:i] + temp[i+1:], subset)
                subset.pop()



        backtrack(nums, [])
        return toRet
        