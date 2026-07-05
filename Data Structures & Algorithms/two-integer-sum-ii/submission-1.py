class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i do not understand how this is different from TwoSum problem
        # 1 - we will olny go upto nums[i] < target
        # 2 - only go upto the number till which is <= target - nums[i]

        for i in range (0, len(numbers)):
            j = i+1
            while (j < len(numbers) and numbers[j] <= target - numbers[i]):
                if (numbers[j] == target - numbers[i]):
                    return [i+1, j+1]
                else:
                    j += 1
            