class Solution:
    def search(self, nums: List[int], target: int) -> int:
        isNumFound = False
        pivot = len(nums)//2
        moveForward = target > nums[pivot]
        while isNumFound == False:
            if pivot < 0 or pivot > len(nums)-1  :
                return -1
            elif nums[pivot] == target:
               return pivot
            # elif pivot == 0 or pivot == len(nums)-1  :
            #     return -1
            elif moveForward:
                pivot +=1
            else :
                pivot -=1
        return -1        
