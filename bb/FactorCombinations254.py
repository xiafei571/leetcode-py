class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def backtrack(n, start, cur):
            if n == 1 and len(cur) > 1:
                res.append(cur)
                return
            
            for i in range(start, n+1):
                if n % i == 0:
                    cur.append(i)
                    backtrack(n//i, i, cur.copy())
                    cur = cur[:-1]
        backtrack(n, 2, [])
        return res