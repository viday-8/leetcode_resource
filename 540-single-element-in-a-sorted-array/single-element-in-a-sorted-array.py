class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0 
        end =len(nums)-1
        if end==0:
            return nums[end]
        while start <= end:
            print(start, end)
            if nums[start] == nums[start+1]:
                start += 2
            elif nums[start] != nums[start+1]:
                return nums[start]     
                
            
            if nums[end] == nums[end-1]:
                end -= 2  
            elif nums[end] != nums[end-1]:
                return nums[end]    
                  
        return nums[0]          