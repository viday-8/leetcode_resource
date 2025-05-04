class Solution(object):
    def twoSum(self, nums, target):
        valueDist = {nums[0] : 0}
        for i in range(1,len(nums)): 
            targetDifference = target-nums[i]
            if targetDifference in valueDist.keys():
                v = valueDist[targetDifference]
                return [v,i]
            valueDist[nums[i]] = i
    
        