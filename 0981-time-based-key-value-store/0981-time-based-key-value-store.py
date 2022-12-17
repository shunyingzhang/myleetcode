class TimeMap:

    def __init__(self):
        self.hashmap = {} # key: [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        value = self.hashmap.get(key, [])
        l = 0
        r = len(value) - 1
        while l <= r:
            m = (l + r) // 2
            if timestamp < value[m][1]:
                r = m - 1
            elif timestamp > value[m][1]:
                res = value[m][0]
                l = m + 1
            else:
                return value[m][0]
        return res
        
        # res = ""
        # value = self.hashmap.get(key, [])
        # l = 0
        # r = len(value) - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if value[m][1] <= timestamp:
        #         res = value[m][0]
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)