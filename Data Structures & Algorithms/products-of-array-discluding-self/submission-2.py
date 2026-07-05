class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # aster = [48, 24, 6, 1]
        len_ = len(nums)
        after = [1]* len_
        before = [1]* len_
        for i in range(len_-1, 0, -1):
            after[i-1] = after[i]*nums[i]
        for i in range(0, len_-1):
            before[i+1] = before[i]*nums[i]
        for i in range(len_):
            after[i] = after[i]*before[i]
        return after
        # print(after)
        # print(before)

        # len_ = len(nums)
        # postfix = [0] * len_
        # prefix = [0] * len_
        # toReturn = [0] * len_
        # postfix[0] = nums[0]
        # for i in range (1, len_):
        #     postfix[i] = postfix[i-1] * nums[i]
        
        # prefix[len_ - 1] = nums[len_ - 1]
        # for i in range(len_ - 2, -1, -1):
        #     prefix[i] = prefix[i+1] * nums[i]

        # # cur = prefix[i-1] * postfix[i+1]
        # for i in range(0, len_):
        #     low = 1 if i-1 < 0 else postfix[i-1]
        #     grt = 1 if i+1 == len_ else prefix[i+1]
        #     toReturn[i] = low * grt
        # return toReturn
            
        