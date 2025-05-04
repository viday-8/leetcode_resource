class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        iterateSum = nums[0]
        for i in range(1,len(nums)):
               iterateSum = max(nums[i], iterateSum+nums[i])
               maxSum = max(maxSum, iterateSum)
        return maxSum             
               