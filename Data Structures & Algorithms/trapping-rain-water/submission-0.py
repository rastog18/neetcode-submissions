class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        prevMax = 0
        maxArray = []
        afterMax = 0
        while(i < len(height)):
            ptr1 = height[i]
            prevMax = max(prevMax, ptr1)
            maxArray.append(prevMax)
            i+=1
        i -= 1
        while(i >= 0):
            ptr1 = height[i]
            afterMax = max(afterMax, ptr1)
            maxArray[i] = min(maxArray[i], afterMax) - height[i]
            i -= 1
        return(sum(maxArray))


        