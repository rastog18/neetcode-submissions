class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        adjList = [0] *26
        for i in tasks:
            adjList[ord(i)-65] -= 1

        heapq.heapify(adjList)
        cooldown = deque([])

        time = 0
        while((adjList and adjList[0] < 0) or cooldown):
            time += 1

            if adjList and adjList[0] < 0:
                toAppend =  heapq.heappop(adjList)+1
                if toAppend < 0:
                    cooldown.append([time + n, toAppend])

            if cooldown and cooldown[0][0] == time:
                toPush = cooldown.popleft()
                heapq.heappush(adjList, toPush[1])

        return time

            
        

        