class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {i : [] for i in range(numCourses)}
        for i in prerequisites:
            preReq[i[0]].append(i[1])
        
        classesChecked = set()
        checking = set()

        def checkClass(i):
            if preReq[i] == [] or i in classesChecked:
                return True
            if i in checking:
                return False

            checking.add(i)
            for c in preReq[i]:
                print(i)
                tc = checkClass(c)
                if not tc:
                    return False
            for j in checking:
                classesChecked.add(j)
            checking.clear()
            return True

        for i in preReq:
            print(classesChecked)
            if i not in classesChecked:
                checking.clear()
                toContinue = checkClass(i)
                    
                if not toContinue:
                    return False
        return True
        