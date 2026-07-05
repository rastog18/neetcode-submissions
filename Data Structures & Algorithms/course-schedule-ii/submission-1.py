class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        orderToFollow = []
        orderToFollowSet = set()
        visited = set()
        visiting = set()

        # Making the adjacecny List
        adjList = {i : [] for i in range(numCourses)}
        for i in prerequisites:
            adjList[i[0]].append(i[1])
        
        # 
        def hasCycle(course):
            if course in visiting:
                return True
            if course in visited:
                return False
            
            visiting.add(course)
            for c in adjList[course]:
                if hasCycle(c):
                    return True
            
            visited.add(course)
            visiting.remove(course)

            if course in visited or adjList[course] == -1:
                if course not in orderToFollowSet:
                    orderToFollow.append(course)
                    orderToFollowSet.add(course)
                    return False

        for course in adjList:
            if hasCycle(course):
                return []

        return orderToFollow
        