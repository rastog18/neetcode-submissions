class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        newHand = sorted(hand)
        handDict = {}
        for i in hand:
            if handDict.get(i) is None:
                handDict[i] = 0
            handDict[i] += 1
        for i in newHand:
            if handDict.get(i) > 0:
                for j in range(groupSize):
                    if handDict.get(i+j)is not None and handDict.get(i+j) > 0:
                        handDict[i+j] -= 1
                    else:
                        return False
        return True
        