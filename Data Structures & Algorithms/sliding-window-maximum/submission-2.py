class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force would be to sort the new list everytime and append the last 
        # integer to the res[]. 
        # To make this more efficient we need to find a way to store the order
        # of the sorted numbers we are not popping.


        #iterate through the array
        # if nums[r] > q[-1] pop unitl that is not the case
        # if r+1 >= k then increment l but before append nums[l] to res
        # if l > q[0] popleft of the queue

        # the best way to handle this is to maintain a queue or a heap
        res = []
        q = deque()
        l = 0
        for r in range(0, len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1

            if l > q[0]:
                q.popleft()
                
        return res
            
                

        