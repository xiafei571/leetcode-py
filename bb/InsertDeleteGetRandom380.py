class RandomizedSet:

    def __init__(self):
        self.arrayList = []
        self.hashMap = {}

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.hashMap[val] = len(self.arrayList)
            self.arrayList.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            idx = self.hashMap[val]
            lastVal = self.arrayList[-1]
            self.arrayList[idx] = lastVal
            self.arrayList.pop()
            self.hashMap[lastVal] = idx
            del self.hashMap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.arrayList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()