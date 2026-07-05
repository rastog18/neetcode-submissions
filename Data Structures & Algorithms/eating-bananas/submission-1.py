class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateHourForRate(rate : int) ->int:
            toReturn = 0
            for i in piles:
                toReturn += math.ceil(i / rate)
            return toReturn

        r = max(piles)
        l = 1
        
        while(l < r):
            toCheck = (l+r)//2
            timeTaken = calculateHourForRate(toCheck)
            if (timeTaken <= h):
                # all times greater to this will work
                r = toCheck
            elif (timeTaken > h):
                l = toCheck + 1
        return l

        