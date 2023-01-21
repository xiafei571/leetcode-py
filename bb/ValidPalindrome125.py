class Solution:
    def isPalindrome(self, s: str) -> bool:
        # brute force
        newStr = ''
        for c in s:
            if self.isAlphaNum(c):
                newStr += c.lower()
        return newStr == newStr[::-1]

    def isAlphaNum(self, c):
        if (ord('A') <= ord(c) <= ord('Z')) or (ord('a') <= ord(c) <= ord('z')) or (ord('0') <= ord(c) <= ord('9')):
            return True
        return False
    