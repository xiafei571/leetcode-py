class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False;
        
        if x == 0:
            return True

        str_x = str(x)
        if str_x[len(str_x) - 1] == '0':
            return False
        
        reverse_str_x = ''
        for ch in str_x[::-1]:
            reverse_str_x += ch

        return str_x == reverse_str_x

    def isPalindrome2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False;
        
        if x == 0:
            return True

        reverted_x = 0
        tmp = x
        while tmp > 0:
            reverted_x = reverted_x * 10 + tmp % 10
            tmp = tmp // 10
         
        return reverted_x == x