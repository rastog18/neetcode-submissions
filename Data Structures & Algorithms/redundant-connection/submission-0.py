class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        adjList = {i:[] for i in range(1, len(edges)+1)}
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        
        visitingList = []
        visitingSet = set()

        def findCircularComponent(node, prev):
            if node in visitingSet:
                from_ = visitingList.index(node)
                return visitingList[from_:]
            
            visitingSet.add(node)
            visitingList.append(node)

            for child in adjList[node]:
                if child != prev:
                    ret = findCircularComponent(child, node)
                    if ret != []:
                        return ret
            visitingSet.remove(node)
            visitingList.pop()
            return []

        redundantConnection = []
        ret = findCircularComponent(1, 0)

        for i,j in edges:
            
            if i in ret and j in ret:
                redundantConnection = [i,j]
        return redundantConnection
