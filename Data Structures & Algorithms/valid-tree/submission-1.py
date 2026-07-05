class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        
        adjList = {i: [] for i in range(n)}
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        
        def DFShasCycle(node, prev):
            if node in visited:
                return True
            
            visited.add(node)
            for child in adjList[node]:
                if child != prev:
                    if DFShasCycle(child, node):
                        return True
            return False
        if n == 0:
            return True

        if DFShasCycle(0, -1) or len(visited) != n:
            return False
            
        return True
        

        