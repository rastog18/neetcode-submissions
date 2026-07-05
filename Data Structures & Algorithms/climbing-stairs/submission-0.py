class Solution:
    def climbStairs(self, n: int) -> int:
        OPT = [1] * (n+1)
        for i in range(2, n+1):
            # print(i)
            # print(OPT[i])
            OPT[i] = (OPT[i-1]) + (OPT[i-2])
            # print(OPT[i])
        # print(OPT)
        return OPT[n]



# OPT[n] - gives the maximum number of ways you can use to reach nth staircase

# OPT[n] = 
# 1 + OPT[n-1] 
# 2 + OPT[n-2]

# Base Case OPT[-ve, 0] = 0
