class Solution:
    def trap(self, height: List[int]) -> int:
        lm = 0 
        rm = height[-1]
        water = 0
        i,j = 0, len(height)-1
        temp = True
        while i<j:
            if temp ==True:
                lm = max(height[i],lm)
                cal = min(lm,rm)-height[i] 
            else:
                rm = max(height[j],rm)
                cal = min(lm,rm)-height[j]
            if cal > 0:
                water += cal
            if height[i]<height[j]:
                temp = True
                i+=1
            else:
                temp =False
                j-=1
        return water
