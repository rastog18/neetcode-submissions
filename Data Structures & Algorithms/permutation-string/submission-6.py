class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create a set for s1, on the first occurance of i in set 
        # create a window /set for s2 of size len(s1) if two sets are equal 
        # return true

        if (len(s1) > len(s2)):
            return False
        
        count = {}
        for i in s1:
            count[i] = 1 + count.get(i, 0)
        

        l = 0
        r = len(s1)
        while(r <= len(s2)):
            count2 = {}
            for i in range(l,r):
                count2[s2[i]] =  1 + count2.get(s2[i], 0)
            if (count2 == count):
                return True
            print(count, count2)

            l+=1
            r+=1
        return False