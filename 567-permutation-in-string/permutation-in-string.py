class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = {}

        for i in s1:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1


        for j in range((len(s2)+1)-len(s1)):
            if s2[j] in s1:
                dic2 = {}
                for k in range(len(s1)):
                    if s2[j+k] in dic2:
                        dic2[s2[j+k]] += 1
                    else:
                        dic2[s2[j+k]] = 1
                print("dic",j, dic1, dic2)        
                if dic1 == dic2:
                    return True 
        return False                    

        