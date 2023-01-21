class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force
        newStr = ''
        for c in s:
            if self.isAlphaNum(c):
                newStr += c.lower()
        return newStr == newStr[::-1]

    def isPalindrome_v2(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def isAlphaNum(self, c):
        if (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
            return True
        return False
    