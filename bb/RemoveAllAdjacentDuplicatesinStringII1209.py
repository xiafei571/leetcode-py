class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] #[char, int]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = ''
        for ch, count in stack:
            res += (ch * count)

        return res

    def removeDuplicates2(self, s: str, k: int) -> str:
        stack = [] #[char, int]
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            elif stack and stack[-1][0] != c:
                # different char
                if stack[-1][1] >= k: #改成while?
                    stack.pop()
                    if stack and stack[-1][0] == c:
                        stack[-1][1] += 1
                    else:
                        stack.append([c, 1])
            else:
                stack.append([c, 1])

        

        res = ''
        for ch, count in stack:
            res += (ch * count)

        return res

if __name__ == "__main__":

    obj = Solution()
    print(obj.removeDuplicates('aaabbbbacc', k=3))

    print(obj.removeDuplicates2('aabbbbacc', k=3))