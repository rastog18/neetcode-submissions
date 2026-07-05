class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [-float("inf"), -float("inf"), -float("inf")]
        for i in triplets:
            if i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2]:
                res[0] = max(res[0], i[0])
                res[1] = max(res[1], i[1])
                res[2] = max(res[2], i[2])
        if res == target:
            return True
        return False