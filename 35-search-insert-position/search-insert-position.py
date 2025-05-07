class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pivot = len(nums)//2
        moveForward = target > nums[pivot]
        while pivot >= 0 and  pivot <= len(nums)+2//2:
            if nums[pivot] == target:
                return pivot
            elif target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0        
            elif moveForward:
                pivot += 1
                if nums[pivot-1]<target < nums[pivot]:
                    return pivot
            else:
                pivot -=1
                if nums[pivot]<target < nums[pivot+1]:
                    return pivot+1 
