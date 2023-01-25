class Solution:
    def isValid(self, s: str) -> bool:
        # ()[]{}
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in mapping: # right
                last = stack.pop() if stack else '' # ']' maybe null?
                if mapping[bracket] != last:
                    return False
            else: # left
                stack.append(bracket)

        return not stack