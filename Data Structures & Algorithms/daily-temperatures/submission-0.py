class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Hint 2 : says we should find an element greater than the current one
        monDec = [[temperatures[0], 0]]
        output = [0] * len(temperatures)
    
        for i in range(1, len(temperatures)):
            while(monDec and temperatures[i] > monDec[-1][0]):
                j = monDec.pop()[1]
                output[j] = i - j
            monDec.append([temperatures[i], i])
        return output
            

        