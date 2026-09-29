class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = sorted(nums)
        count = 1
        res = 0

        if not nums:
            return 0
        for i in range(1,len(snums)):
            if snums[i]-snums[i-1]==1:
                count+=1
                res = max(res,count)
            elif snums[i]-snums[i-1]==0:
                count+=0
                res = max(res,count)
            else:
                count = 1
        return max(res,count)
            

