class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        toRet = []
        subset = []
        candidates.sort()

        def backTrack(i, subset, total):
            if target == total:
                toRet.append(subset.copy())
                return
            if target < total or i >= len(candidates):
                return
            
            subset.append(candidates[i])
            backTrack(i+1, subset, total+candidates[i])
            subset.pop()
            while (i+1 < len(candidates) and candidates[i+1] == candidates[i]):
                i += 1
            backTrack(i+1, subset, total)
        backTrack(0, [], 0)

        
        return toRet

        