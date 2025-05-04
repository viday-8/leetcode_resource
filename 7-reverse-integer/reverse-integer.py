class Solution:
    def reverse(self, x: int) -> int:
        num=str(abs(x))
        y=num[::-1]
        if -2**31 <= int(y) <= 2**31 - 1 :
            if(x >= 0):
                return int(y)
            else:
                return -1*int(y)
        else:
            return 0

            
          
