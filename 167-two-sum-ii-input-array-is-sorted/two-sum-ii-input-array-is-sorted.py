class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        refOne = 0
        refTwo = len(numbers)-1
        while refOne<refTwo:
            sumD = numbers[refOne]+numbers[refTwo]
            if sumD == target:
                return [refOne+1,refTwo+1]
            elif sumD > target:
                refTwo -= 1
            elif sumD < target:
                refOne +=1
