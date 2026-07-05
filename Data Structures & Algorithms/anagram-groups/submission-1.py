class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """# create an adjacecny list for all strings - O(n)
        # compare and add to the new list if same 
        #space - O(n)
        adjList = {}
        toReturn = []
        for i in strs:
            temp = {}
            for j in i:
                temp[j] = 1 + temp.get(j, 0)
            
            #toReturn[temp] = toReturn.get(temp, []).append(i)
            adjList[i] = temp
            append = False
            for ind,item in enumerate(toReturn):
                if adjList[item[0]] == temp:
                    toReturn[ind].append(i)
                    append = True
            if (append == False):
                toReturn.append([f"{i}"])
        
        return toReturn
        """
    
        toReturn = {}
        for i in strs:
            count = [0] * 26 
            for c in i:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            
            toReturn.setdefault(key, []).append(i)
        return list(toReturn.values())  