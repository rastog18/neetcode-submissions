class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while (l < r):
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
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


        