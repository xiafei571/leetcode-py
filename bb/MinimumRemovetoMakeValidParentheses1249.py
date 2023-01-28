class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        split_str=list(s)
        for idx in range(len(s)):
            if s[idx] == '(':
                stack.append(idx)
            elif s[idx] == ')':
                if len(stack) == 0:
                    split_str[idx] = ''
                else:
                    stack.pop()
        
        while stack:
            split_str[stack.pop()] = ''
        
        return ''.join(split_str)