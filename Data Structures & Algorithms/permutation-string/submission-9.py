class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a set for s1, on the first occurance of i in set 
        # create a window /set for s2 of size len(s1) if two sets are equal 
        # return true
        def checkValidity(index):

            temp = {}
            r = index + len(s1)
            if r > len(s2):
                return False
            for itr in range(index, r):
                temp[s2[itr]] = temp.get(s2[itr], 0) + 1

            if temp == count:
                return True
            return False
        
        count = {}
        for i in s1:
            count[i] = 1 + count.get(i, 0)
        
        for i in range(len(s2)):
            if (count.get(s2[i], -1) != -1) and checkValidity(i):
                return True
        return False
        # l = 0
        # r = len(s1)
        # while(r <= len(s2)):
        #     count2 = {}
        #     for i in range(l,r):
        #         count2[s2[i]] =  1 + count2.get(s2[i], 0)
        #     if (count2 == count):
        #         return True
        #     print(count, count2)

        #     l+=1
        #     r+=1
        # return False