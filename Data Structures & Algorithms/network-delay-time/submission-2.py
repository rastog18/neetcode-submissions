class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # run Dijikstra
        # return max(resDijikstra)
        neighbors = {}
        for u, v, t in times:
            if u not in neighbors:
                neighbors[u] = []
            neighbors[u].append((v, t))
        
        # while accessing dist or prev search for dist[i-1] instead of dist[i]
        dist = [float("inf") for i in range(n)]

        dist[k-1] = 0
        minHeap = []
        heapq.heappush(minHeap, (0, k))

        while(minHeap):
            d, n = heapq.heappop(minHeap)

            if d > dist[n-1]:
                continue

            for to, time in neighbors.get(n, []):
                alt = d + time
                if alt < dist[to-1]:
                    dist[to-1] = alt
                    heapq.heappush(minHeap, (dist[to-1], to))

        if max(dist) == float("inf"):
            return -1
        else:
            return max(dist)
            