class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0,len(heights)-1
        maxar = 0
        while i<j:
            area = min(heights[i],heights[j])*(j-i)
            maxar = max(maxar, area)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxar
