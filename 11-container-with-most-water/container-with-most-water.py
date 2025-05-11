class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        area = 0
        while start < end:
            l = end - start
            if height[start] < height[end]:
                a = l* height[start]
                area = max(area, a)
                start += 1
            elif height[end] < height[start]:
                a = l* height[end]
                area = max(area, a)
                end -=1
            else:
                a = l* height[end]
                area = max(area, a)
                end -=1
                start += 1 
        return area          