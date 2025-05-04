class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returnArr = []
        product = prod(nums)
        print(product)
        for i in range(len(nums)):
            p = 1
            if nums[i] == 0:
                for j in range(len(nums)):
                    if j !=i:
                        p = p*nums[j]
            else :
                p = int(product/nums[i])
            returnArr.append(p)  
        return returnArr         
        