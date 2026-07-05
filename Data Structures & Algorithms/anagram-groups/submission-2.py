class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a set of all strings
        #create a hashmap (set -> index)
        # for a new set encounter add it to RetList
        toRet = []
        adjList = {} #set -> index

        for s in strs:
            temp = tuple(sorted(s))
            index = adjList.get(temp, -1)
            # print(s)
            # print(temp)
            # print(index)
            # print(adjList)
            # print(toRet)
            # print()
            if index == -1:
                toRet.append([s])
                adjList[temp] = len(toRet) - 1
            else:
                toRet[index].append(s)
        return toRet