class Solution:
    def reverse(self, x: int) -> int:
        num=str(x)
        length=len(num)
        start=0
        new=""
        new_num=0
        if num[0]=="-":
            new+=num[0]
            start=1
        for i in range(length-1,start-1,-1):
            new+=str(int(num[i])%10)
        y=int(new)
        if y<-2**31 or y>=2**31:
            return 0
        
        return y

            
          
