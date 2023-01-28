class Solution:
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