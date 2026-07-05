class TimeMap:

    def __init__(self):
        self.adjList = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.adjList.get(key):
            self.adjList[key].append([value, timestamp])
        else:
            self.adjList[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if self.adjList.get(key):
            values = self.adjList[key]
            l = 0
            r = len(values) - 1
            cur = ""
            while(l <= r):
                # we to have find a pair with TIME <= given TIMESTAMP
                mid = (l+r)//2
                if (values[mid][1] == timestamp):
                    return values[mid][0]
                elif (values[mid][1] < timestamp):
                    l = mid + 1
                    cur = values[mid][0]
                else:
                    r = mid - 1
            return cur
        else:
            return ""
        
