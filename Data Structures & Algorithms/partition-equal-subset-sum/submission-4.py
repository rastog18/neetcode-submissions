class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Necessary variables
        n = len(nums)
        OPT = [0]
        aim = sum(nums)

        # If the totalSum is an odd number it can never have two equal subsets
        if aim%2 != 0:
            return False
        aim = aim / 2

        for num in nums:
            print(num)
            print()
            for n in range(len(OPT)):
                # print(OPT)
                # print(n)
                toAdd = OPT[n] + num
                if toAdd < aim:
                    OPT.append(toAdd)
                elif toAdd == aim:
                    print(toAdd)
                    return True
        
        return False
