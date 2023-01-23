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
        