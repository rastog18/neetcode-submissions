class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        greedyList = [cost[i]-gas[i] for i in range(len(gas))]
        curSum = 0
        start = 0
        for i in range(len(gas)):
            curSum += greedyList[i]
            if curSum > 0:
                curSum = 0
                start = i+1
        if start >= len(gas):
            return -1
        for i in range(0, start):
            curSum += greedyList[i]
            if curSum > 0:
                return -1
        return start

        