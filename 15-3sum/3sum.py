class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
         
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            start = i+1
            end =len(nums)-1
           
            while start < end:
                b = nums[start]
                c = nums[end]
                d = [a,b,c]
                if b+c == -a :
                    triplets.append([a,b,c])
                    start += 1
                    while nums[start] == nums[start-1] and start < end:
                        start +=1 

                elif b+c > -a :
                    end -=1
                else:
                    start += 1

        return triplets           