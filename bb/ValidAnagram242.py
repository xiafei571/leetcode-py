class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
         
        s_cnt = [0] * 26
        for ch in s:
            s_cnt[ord(ch) - ord('a')] += 1

        for ch in t:
            if s_cnt[ord(ch) - ord('a')] <= 0:
                return False
            else:
                s_cnt[ord(ch) - ord('a')] -= 1

        return True