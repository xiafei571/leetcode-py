class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLen = 0, 0, 0
        hashMap = {}
        
        for r in range(len(s)):
            if s[r] not in hashMap:
                maxLen = max(maxLen, r - l + 1)
                # print(1, l, r, maxLen)
            else:
                if hashMap[s[r]] < l: # not in current window
                    maxLen = max(maxLen, r - l + 1)
                    # print(2, l, r, maxLen)
                else:
                    l = hashMap[s[r]] + 1
            hashMap[s[r]] = r

        return maxLen