class UnionFind:
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size))
    
    def find(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
          
        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])
    
    def unite(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edgesHeap = []
        for i, p in enumerate(points):
            for j, p2 in enumerate(points):
                if p != p2:
                    dist = abs(p[0] - p2[0]) + abs(p[1] - p2[1])
                    heapq.heappush(edgesHeap, (dist, i, j))
        
        uf = UnionFind(len(points))
        res = 0
        while len(edgesHeap) > 0:
            dist, i, j = heapq.heappop(edgesHeap)
            if uf.find(i) != uf.find(j):
                uf.unite(i, j)
                res += dist
        return res

        