class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = len(nums)//2
        moveForward = target > nums[pivot]
        while pivot >= 0 and pivot <= len(nums)-1:
            if nums[pivot] == target:
               return pivot
            elif moveForward:
                pivot +=1
            else :
                pivot -=1
        return -1        
