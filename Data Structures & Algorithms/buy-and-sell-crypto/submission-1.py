class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to find the largest difference of two pair subsequence
        # calculate a curProfit for each valid sliding window and return the maxProfit
        maxProfit = 0
        profit = 0
        l, r = 0,1
        if len(prices) == 1:
            return maxProfit

        while (l < len(prices)):
            profit = (prices[r] - prices[l])
            maxProfit = max(maxProfit, profit)
            print(l)
            print(r)
            print(profit)
            print()
            if r+1 < len(prices) and l == r:
                r += 1
            elif l+1 < len(prices) and prices[l] >= prices[r]:
                #invalid window
                l += 1
            elif r+1 < len(prices):
                r += 1
            else:
                break
        return maxProfit









        # brute force approach - loop 1 assumes we the buy the price at 
        # that index, then we iterate loop 2 through all values, trying to 
        # find max(prices[i] - prices[j]) and storeit in maxSale
        # we repeadly do this for all price[i] values

        # subtract current from next if negative continue
        # if positive continue and add difference to res and return res
        res = 0
        maxRes = 0
        for i in range(0, len(prices)-1):
            cur = prices[i]
            dif =  prices[i+1] - cur
            if (dif + res < 0):
                res = 0
            else:
                res += dif
            maxRes = max(maxRes, res)
        return maxRes

        