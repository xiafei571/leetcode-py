class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         map = {}

         for i in range(len(nums)):
             rest = target - nums[i]
             if rest in map.keys():
                 return [i, map[rest]]
             
             map[nums[i]] = i
        