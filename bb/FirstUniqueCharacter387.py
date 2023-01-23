class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = collections.defaultdict(int)
        for ch in s:
            map[ch] += 1
        
        for idx in range(len(s)):
            if map[s[idx]] == 1:
                return idx

        return -1
            