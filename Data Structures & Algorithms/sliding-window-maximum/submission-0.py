class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force would be to sort the new list everytime and append the last 
        # integer to the res[]. 
        # To make this more efficient we need to find a way to store the order
        # of the sorted numbers we are not popping.

        onHand = nums[:k]
        onHand.sort()
        res = []
        res.append(onHand[k-1])

        for i in range(0, len(nums)-k):
            toPop = nums[i]
            toAdd = nums[i+k]
            onHand.remove(toPop) # - O(k)
            for j in range(k): # - O(k)
                if (j == k-1):
                    onHand.append(toAdd)
                    break
                if (toAdd < onHand[j]):
                    onHand.insert(j, toAdd)
                    break
            res.append(onHand[k-1])
        
        return res
                

        