class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pivot = len(nums)//2
        moveForward = target > nums[pivot]
        diff = 0
        while pivot >= 0 and  pivot <= len(nums)+2//2:
            if nums[pivot] == target:
                return pivot
            elif target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0        
            # elif nums[pivot-1] < target < nums[pivot+1]  :
            #     print("pivot", pivot)
            #     return pivot
            elif moveForward:
                pivot += 1
                print(nums[pivot-1],nums[pivot])
                if nums[pivot-1]<target < nums[pivot]:
                    print("m", pivot)
                    return pivot
                print("mm",pivot)  
            else:
                pivot -=1
                if nums[pivot]<target < nums[pivot+1]:
                    print("b", pivot+1)
                    return pivot+1 
                print("BB",pivot) 