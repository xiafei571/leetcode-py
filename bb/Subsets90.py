class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                 res.append(cur.copy())
                 return

            #skip the duplicates, except for the first time
            
            # all subsets include nums[i]
            cur.append(nums[i])
            dfs(i+1)
            # all subsets do not include nums[i]
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
            
        dfs(0)
        return res