class Solution:

     def rob_spaceO1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0 # rob1, rob2, n, n+1 ...
        for n in nums:
            tmp = max(rob2, n+rob1)
            rob1 = rob2
            rob2 = tmp

        return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(nums[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]