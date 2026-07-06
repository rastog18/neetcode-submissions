class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # we maintain a list of monotonically decreasing temperatures
        # when we pop from this md we updaate the result to that day
        # maybe we store the indecides in the temp
        result = [0] * len(temperatures)
        monDec = []
        for i, j in enumerate(temperatures):
            while len(monDec) != 0 and j > temperatures[monDec[-1]]:
                index = monDec.pop()
                result[index] = i - index
            monDec.append(i)
        return result





        # Hint 2 : says we should find an element greater than the current one
        # monDec = [[temperatures[0], 0]]
        # output = [0] * len(temperatures)
    
        # for i in range(1, len(temperatures)):
        #     while(monDec and temperatures[i] > monDec[-1][0]):
        #         j = monDec.pop()[1]
        #         output[j] = i - j
        #     monDec.append([temperatures[i], i])
        # return output
            

        