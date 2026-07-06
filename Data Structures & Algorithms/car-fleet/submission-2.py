class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posToSpd = {}
        monDec = [] #index -> time
        
        time = [0] * len(speed)

        for i in range(len(speed)):
            posToSpd[position[i]] = speed[i]

        position.sort()
        for i in range(len(speed)):
            time[i] = target - position[i]
            time[i] /= posToSpd[position[i]]
        # print(time)
        for i in range(len(speed)):
            while len(monDec) != 0 and time[i] >= monDec[-1]:
                monDec.pop()
            monDec.append(time[i])
        # print(monDec)
        return len(monDec)
        
        
        # adjList = {}
        # len_fleet = len(position)
        # for i,j in enumerate(position):
        #     adjList[j] = speed[i]
        
        # position.sort()

        # fleet = [position[-1]]
        # for i in range(len_fleet-1, 0, -1):
    
        #     carF = fleet[-1]
        #     carf = position[i - 1]
        
        #     if ((target - carF) / adjList[carF]) < ((target - carf) / adjList[carf]):
        #         # Fleet is not formed - so we add car to the list of distinct fleets
        #         fleet.append(carf)
        
        # return len(fleet)
                
        



        