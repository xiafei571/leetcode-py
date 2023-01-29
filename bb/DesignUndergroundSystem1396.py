class UndergroundSystem:

    def __init__(self):
        self.user = {} # {id, (stationName, startTime)}
        self.station = collections.defaultdict(list) # {(start, end), list(time))}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = ((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.user[id]
        self.station[(startStation, stationName)].append(t - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg_list = self.station[(startStation, endStation)]
        if avg_list:
            return sum(avg_list) / len(avg_list)
        else:
            return 0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)