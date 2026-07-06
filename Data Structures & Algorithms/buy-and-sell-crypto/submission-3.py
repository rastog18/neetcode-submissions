class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we want to find the largest difference of two pair subsequence
        # calculate a curProfit for each valid sliding window and return the maxProfit
        # if we keep track of the minimum value encountered till now and subtract it from every new price
        minPrice = 101
        maxProfit = 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
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

        