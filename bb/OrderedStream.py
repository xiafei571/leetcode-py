class OrderedStream:

    def __init__(self, n: int):
        self.arr = [''] * (n + 1)
        self.n = n
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.arr[idKey] = value
        while self.ptr <= self.n and self.arr[self.ptr] != '':
            res.append(self.arr[self.ptr])
            self.ptr += 1

        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
