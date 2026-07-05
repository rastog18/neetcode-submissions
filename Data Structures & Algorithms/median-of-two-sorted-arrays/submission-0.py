class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tLen = len(nums1) + len(nums2)
        mAt = tLen // 2
        m = -1
        n = -1
        cur = -1
        l1 = 0
        l2 = 0
        for i in range(mAt + 1):
            if l1 >= len(nums1):
                cur = nums2[l2]
                l2 += 1
            elif l2 >= len(nums2):
                cur = nums1[l1]
                l1 += 1
            elif nums1[l1] < nums2[l2]:
                cur = nums1[l1]
                l1 += 1
            else:
                cur = nums2[l2]
                l2 += 1
            if i == mAt-1:
                m = cur
            if i == mAt:
                n = cur
        #     print(cur)
        # print(m)
        # print(n)
        if tLen % 2 == 0:
            return (n+m)/2
        else:
            return n
