class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i : [] for i in range(numCourses)}
        for i in prerequisites:
            preReq[i[0]].append(i[1])
        
        classesChecked = set()
        checking = set()

        def hasCycle(course):
            if preReq[course] == [] or course in classesChecked:
                return False

            if course in checking:
                return True

            checking.add(course)

            for c in preReq[course]:
                if hasCycle(c):
                    return True

            classesChecked.add(course)
            checking.remove(course)
            return False

        for course in preReq:
            if hasCycle(course):
                return False

        return True
        