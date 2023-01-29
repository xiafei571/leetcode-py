class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        
        diffs.sort(key = lambda x : x[0])

        sum = 0
        for i in range(len(diffs)):
            if i < len(diffs)//2:
                sum += diffs[i][2]
            else:
                sum += diffs[i][1]
        return sum