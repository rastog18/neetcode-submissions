class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        
        adjList = {i: [] for i in range(n)}
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])

        def DFS(node, prev):
            visited.add(node)
            for child in adjList[node]:
                if child not in visited:
                    DFS(child, node)
        
        connectedNodes = 0
        for i in range(n):
            if i not in visited:
                DFS(i, -1)
                connectedNodes += 1
        return connectedNodes