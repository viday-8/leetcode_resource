class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstO = -1
        lastO = -1
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[start] == target and nums[end] == target:
                return [start,end]
            elif nums[start] < target:
                start += 1
            else:
                end -= 1
        return [firstO, lastO]                    
        